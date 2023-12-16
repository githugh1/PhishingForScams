import json
from main_script import predict_spam, train_spam_model


#obviously will have proper csv but use below for now...
train_data = [
    "Congratulations! You've won a free iPhone...",
    "Enlarge your savings with our exclusive offers...",
    "Important business proposal: lucrative opportunity..."
]

train_labels = [1, 1, 0]  # 1: Spam, 0: Not Spam

# train model
spam_model = train_spam_model(train_data, train_labels)

# function to iterate over tests
def run_tests():
    test_case_number = 1
    while True:
        input_file = f'tests/test_cases/test_case{test_case_number}.in'
        output_file = f'tests/test_cases/test_case{test_case_number}.out'

        try:
            with open(input_file, 'r') as f:
                test_case = json.load(f)

            with open(output_file, 'r') as f:
                expected_output = json.load(f)

            input_features = [
                f"{test_case['email_subject']} {test_case['email_body']}"
            ]
        except Exception as e:
            print(e)

