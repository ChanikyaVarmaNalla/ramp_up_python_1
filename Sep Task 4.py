import json

class Employee:
    def __init__(self, employee):
        self.employee = employee
        print(f"I am in {self.__class__.__name__} Init")

    def get_info(self):
        return f"Employees of XYZ Company: {self.employee}"

class Manager(Employee):
    def __init__(self, employee):
        super().__init__(employee)

    def get_info(self):
        manager_info = [emp for emp in self.employee["employees"] if emp["position"] == "Manager"]
        header = "Employees of XYZ Company who are Managers:"
        return f"{header}  {[i['name'] for i in manager_info]}"

class Developer(Employee):
    def __init__(self, employee):
        super().__init__(employee)

    def get_info(self):
        developer_info = [emp for emp in self.employee["employees"] if emp["position"] == "Developer"]
        header = "Employees of XYZ Company who are Developers:"
        return f"{header}  {[i['name'] for i in developer_info]}"

with open("employee_data.json", "r+") as rd:
    data = json.load(rd)

# Employees who are Managers
mana = Manager(data)
print(mana.get_info())

# Employees who are Developers
deve = Developer(data)
print(deve.get_info())
