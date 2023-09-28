# Define a class to represent a customer account
class CustomerAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.__balance = balance
        self.owner_name = owner_name

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        print(f"\nSetting balance to {new_balance}")
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Error: Balance cannot be negative.")

    def display_info(self):
        print("\nAccount Info:")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.get_balance()}")

account1 = CustomerAccount("123456789", 5000.0, "John Doe")
account1.display_info()

account1.set_balance(5500.0)
account1.display_info()

account1.set_balance(-1000.0)
