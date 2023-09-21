import random
import string

class UsernameGenerator:
    def __init__(self, length=8):
        self.length = length
        self.used_usernames = []

    def generate_username(self):
        first_character = random.choice(string.ascii_letters)
        rest_characters = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.length - 1))
        return first_character + rest_characters

    def unique_username_generator(self):
        while True:
            username = self.generate_username()
            if username not in self.used_usernames:
                self.used_usernames.append(username)
                yield username

if __name__ == "__main__":
    username_gen = UsernameGenerator()
    for i in range(int(input("Number of Usernames to be Generated: "))):
        unique_username = next(username_gen.unique_username_generator())
        print("Generated Username:", unique_username)
