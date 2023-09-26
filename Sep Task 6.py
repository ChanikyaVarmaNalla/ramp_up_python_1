class UserProfile:
    def __init__(self, username, email, age):
        self.profile = {
            'username': username,
            'email': email,
            'age': age
        }

    def update_profile(self, new_data):
        try:
            # Check if the 'email' key exists in new_data before updating
            if 'email' in new_data:
                self.profile['email'] = new_data['email']

            # Check if the 'age' key exists in new_data before updating
            if 'age' in new_data:
                self.profile['age'] = new_data['age']

            # Merge other data in new_data into the profile
            for key, value in new_data.items():
                if key not in ('email', 'age'):
                    self.profile[key] = value

            print("\nProfile updated successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_profile(self):
        return self.profile


# Example usage:
user = UserProfile('john_doe', 'john@example.com', 30)

# Display the old data
old_profile = user.get_profile()
print("Old Profile Data:")
print(old_profile)

new_data = {
    'email': 'john.doe@example.com',
    'age': 31,
    'city': 'New York',
    'hobbies': ['hiking', 'reading']
}

user.update_profile(new_data)

# Display the updated data
updated_profile = user.get_profile()
print("\nUpdated Profile Data:")
print(updated_profile)
