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
from utils.pfs_logging import log, log_level, env


class AITrainer:

    __default_config = {
        'data': {
            'file_path': None
        },
        'model': {
            'epochs': 10,
            'batch_size': 32
        },
        'test': {
            'test_size': 0.2,
            # Pass an int for reproducible output across multiple
            # function calls
            'random_state': 42 if env != 'production' else None
        }
    }

    def __init__(self, config_path=None):

        # TODO: check if the config and trainig file exist and
        # confirm to certain format!
        self.config = self.__default_config
        if config_path:
            self.load_config(config_path)

        self.df = pd.DataFrame({})  # empty df!
        self.df_status = 'empty'
        self.model = Sequential()  # empty model!

        self.nltk = nltk
        self.nltk.download('punkt')
        self.nltk.download('stopwords')
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = log_level

    def load_config(self, config_path):
        # loading config
        if config_path and os.path.isfile(config_path):
            f = config_path
        with open(f, 'r') as file:
            config = yaml.safe_load(file)

        for key, value in config:
            if key in self.__default_config:
                self.config[key] = value

        # check if the data_file exists
        if not os.path.isfile(self.config['data']['file_path']):
            log.error(f"cant file {self.config['data']['file_path']}")
            # TODO: setting this to default value for now
            # can do something better!
            self.config['data']['file_path'] = \
                self.__default_config['data']['file_path']

    def load_model(self, model_path=None):
        # TODO: loads an exisiting model for additional training
        pass

    def save_model(self, model_path=None):
        # TODO: saves a trained model to be loaded by the scanners
        pass

    def load_data(self, file_path=None):

        if self.df_status != 'empty':
            log.warning(f'dataframe is not empty, \
                        overriding current status:{self.df_status}')

        f = self.config['data']['file_path']
        if file_path and os.path.isfile(file_path):
            f = file_path

        # f can be None by default!
        if f:
            self.df = pd.read_csv(f)
            self.def_status = 'loaded'
        return self.df

    def preprocess_data(self):
        if self.df_status != 'loaded':
            log.error(f'dataframe is not loaded, \
                      current status:{self.df_status}')
            # TODO: do something!

        stop_words = set(stopwords.words('english'))
        stemmer = PorterStemmer()

        # Tokenization
        self.df['body'] = self.df['body'].apply(lambda x: word_tokenize(x.lower()))

        # remove stop words/ punctuation
        self.df['body'] = self.df['body'].apply(lambda x: [word for word in x if (word not in stop_words and word not in string.punctuation)])

        # Stemming
        self.df['body'] = self.df['body'].apply(lambda x: [stemmer.stem(word) for word in x])

        # combine tokens into sentenc
        self.df['body'] = self.df['body'].apply(lambda x: ' '.join(x))

        self.df_status = 'preprocessed'

        return self.df

    def split_data(self):
        if self.df_status != 'preprocessed':
            log.error(f'dataframe is not preprocessed, \
                      current status:{self.df_status}')
            # TODO: do something!

        train_df, test_df = train_test_split(self.df, test_size=self.config['test']['test_size'], random_state=self.config['test']['random_state'])
        return train_df, test_df

    def vectorize_text(self, train_texts, test_texts):
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        X_train = tfidf_vectorizer.fit_transform(train_texts).toarray()
        X_test = tfidf_vectorizer.transform(test_texts).toarray()
        return X_train, X_test

    def build_model(self, input_dim):
        self.model.add(Dense(128, input_dim=input_dim, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return self.model

    def train_model(self, config_path=None):

        # load config
        if config_path and os.path.isfile(config_path):
            self.load_config(config_path)
        f = self.config['data']['file_path']
        with open(f, 'r') as file:
            config = yaml.safe_load(file)

        # load/preprocess data
        df = self.load_data(config['data']['file_path'])
        df = self.preprocess_data(df)
        train_df, test_df = self.split_data(df)

        # vectorize text
        X_train, X_test = self.vectorize_text(train_df['body'], test_df['body'])

        # build/compile  model
        input_dim = X_train.shape[1]
        self.model = self.build_model(input_dim)

        # choo choo
        self.model.fit(X_train, train_df['label'], epochs=config['model']['epochs'], batch_size=config['model']['batch_size'])

        # generalize to test?
        loss, accuracy = self.model.evaluate(X_test, test_df['label'])
        log.info(f'Test Loss: {loss}, Test Accuracy: {accuracy}')


if __name__ == '__main__':
    ait = AITrainer('config.yaml')
    ait.train_model()
