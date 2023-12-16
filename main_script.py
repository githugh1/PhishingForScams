from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd


csv_file = "" #kaggle csv file, or we can webscrape?? 

# loading and preprocessing (changes based on contents of csv)
def load_and_preprocess_data(data_path):
    # Assuming a CSV file with columns: "email_subject", "email_body", "label"
    df = pd.read_csv(data_path)
    X = df[['email_subject', 'email_body']]
    y = df['label']
    return X, y


# i think the random state has to be the same i.e. the section of data we train on needs to be specified and the same in all iterations of the model... 
def train_spam_model(X_train, y_train):
    model = make_pipeline(TfidfVectorizer(sublinear_tf=True, stop_words='english'), RandomForestClassifier(n_estimators=100))
    model.fit(X_train, y_train)
    return model

# might need to do some cross validation techniques before evaluation
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return accuracy, report

# Example usage
if __name__ == "__main__":
    #will need to implement data cleaning before this
    X, y = load_and_preprocess_data(csv_file)

    # split into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # fit model to training data
    spam_model = train_spam_model(X_train, y_train)

    # test the model, which has been adjusted to train data and see if it can generalise to test data
    accuracy, report = evaluate_model(spam_model, X_test, y_test)

    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

    # e.g tc
    test_email = pd.DataFrame( {'email_subject': ['Special offer inside'], 'email_body': ['Claim your prize now!']})
    prediction = spam_model.predict(test_email)

    print("Example Test Prediction:", prediction[0])
