import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import nltk
import os

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # Tokenization
    df['body'] = df['body'].apply(lambda x: word_tokenize(x.lower()))

    # remove stop words/ punctuation
    df['body'] = df['body'].apply(lambda x: [word for word in x if (word not in stop_words and word not in string.punctuation)])

    # Stemming
    df['body'] = df['body'].apply(lambda x: [stemmer.stem(word) for word in x])

    # combine tokens into sentenc
    df['body'] = df['body'].apply(lambda x: ' '.join(x))

    return df

def split_data(df):
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    return train_df, test_df

def vectorize_text(train_texts, test_texts):
    tfidf_vectorizer = TfidfVectorizer(max_features=5000)
    X_train = tfidf_vectorizer.fit_transform(train_texts).toarray()
    X_test = tfidf_vectorizer.transform(test_texts).toarray()
    return X_train, X_test

def build_model(input_dim):
    model = Sequential()
    model.add(Dense(128, input_dim=input_dim, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(config_path):
    # ;oad config
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # load/preprocess data
    df = load_data(config['data']['file_path'])
    df = preprocess_data(df)
    train_df, test_df = split_data(df)
    
    # vectorize text
    X_train, X_test = vectorize_text(train_df['body'], test_df['body'])
    
    # build/compile  model
    input_dim = X_train.shape[1]
    model = build_model(input_dim)
    
    # choo choo
    model.fit(X_train, train_df['label'], epochs=config['model']['epochs'], batch_size=config['model']['batch_size'])

    # save trained model to  path specified in config
    model.save(config['model']['trained_model_path'])

    # generalize to test?
    loss, accuracy = model.evaluate(X_test, test_df['label'])
    print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('stopwords')
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
  
    train_model('config.yaml')
