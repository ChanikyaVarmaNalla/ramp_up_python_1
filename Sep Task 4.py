import json

class Employee:
    def __init__(self):
        with open("employee_data.json", "r+") as rd:
            self.data = json.load(rd)
        print(f"I am in {self.__class__.__name__} Init")

    def get_info(self):
        return f"Employees of XYZ Company: {self.data}"

class Manager(Employee):
    def __init__(self):
        super().__init__()

    def get_info(self):
        manager_info = [emp for emp in self.data["employees"] if emp["position"] == "Manager"]
        return f"Employees of XYZ Company who are Managers: {[i['name'] for i in manager_info]}"

class Developer(Employee):
    def __init__(self):
        super().__init__()

    def get_info(self):
        developer_info = [emp for emp in self.data["employees"] if emp["position"] == "Developer"]
        return f"Employees of XYZ Company who are Developers: {[i['name'] for i in developer_info]}"

# Employees who are Managers
mana = Manager()
print(mana.get_info())

# Employees who are Developers
deve = Developer()
print(deve.get_info())
