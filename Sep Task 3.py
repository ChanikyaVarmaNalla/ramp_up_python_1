import re

class EmailExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.email_pattern = r'[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'

    def extract_emails(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
            return re.findall(self.email_pattern, text)

if __name__ == "__main__":
    email_extractor = EmailExtractor('document.txt')
    email_addresses = email_extractor.extract_emails()
    for email in email_addresses:
        print(email)
