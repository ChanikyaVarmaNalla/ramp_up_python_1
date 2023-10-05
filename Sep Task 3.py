import re

class EmailExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.email_pattern = r'[A-Za-z][A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[A-Za-z]{2,}'

    def extract_emails(self):
        emails = []
        with open(self.file_path, 'r') as file:
            for line in file:
                line_emails = re.findall(self.email_pattern, line)
                emails.extend(line_emails)
        return emails

if __name__ == "__main__":
    email_extractor = EmailExtractor('document.txt')
    email_addresses = email_extractor.extract_emails()
    for email in email_addresses:
        print(email.lower())
