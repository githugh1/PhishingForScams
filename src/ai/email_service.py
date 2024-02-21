import json
import yaml
import pandas as pd
from confluent_kafka import Consumer, KafkaException
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_email(email_body):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # tokenize
    email_tokens = word_tokenize(email_body.lower())

    # remove stop words
    email_tokens = [word for word in email_tokens if (word not in stop_words and word not in string.punctuation)]

    # stemming
    email_tokens = [stemmer.stem(word) for word in email_tokens]

    # join tokens
    preprocessed_email = ' '.join(email_tokens)

    return preprocessed_email

def vectorize_text(text, tfidf_vectorizer):
    return tfidf_vectorizer.transform([text]).toarray()

def consume_from_kafka(config_path):
    # config
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # load trained model
    model_path = config['model']['trained_model_path']
    model = load_model(model_path)

    # creates Kafka consumer
    consumer_conf = {
        'bootstrap.servers': config['kafka']['bootstrap_servers'],
        'group.id': 'email_consumer_group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_conf)

    # subscribe to the kafka topic
    consumer.subscribe([config['kafka']['topic']])

    # Create TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)

    try:
        while True:
            # poll messages from Kafka
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    # End of partition event, not an error
                    continue
                else:
                    print(msg.error())
                    break

            # decode/preprocess email body
            email_body = json.loads(msg.value())['body']
            preprocessed_email = preprocess_email(email_body)

            #vectorize preprocessed email text
            vectorized_text = vectorize_text(preprocessed_email, tfidf_vectorizer)

            # determine whether spam
            prediction = model.predict(vectorized_text)

            # Output the result
            print(f"Email Prediction: {prediction}")

    except KeyboardInterrupt:
        pass
    finally:
        # close Kafka consumer
        consumer.close()

if __name__ == '__main__':
    consume_from_kafka('config.yaml')