# ramp_up_python_1

Task 1:
1. Created a class AreaCalculator with two methods: calculate_area and get_user_input to encapsulate area calculation and user input collection logic.
2. Created an object calculator from the AreaCalculator class to use its methods.
3. Used the get_user_input method to collect user input values required for calculating the area, which continues until the user enters "end" or three values are collected.
4. Calculated the area based on the number of inputs provided by calling the calculate_area method.
5. Checked the number of values collected in value_list to determine whether to print the area of a circle, rectangle, or triangle based on the length of value_list.

Task 2:
1. Created a class UsernameGenerator to encapsulate username generation logic. Added an __init__ method to initialize the length of usernames and a list used_usernames to keep track of generated usernames.
2. Defined a generate_username method to create random usernames. The first character is chosen randomly from letters, and the rest are chosen randomly from letters and digits.
3. Created a generator method unique_username_generator that yields unique usernames indefinitely.
4. Inside the __main__ block, created an instance username_gen of the UsernameGenerator class. Prompted the user to input the number of usernames to be generated.
6. Used a for loop to generate the specified number of unique usernames by calling next(username_gen.unique_username_generator()) and printed each generated username.

Task 3:
1. Created a class EmailExtractor to handle email address extraction. In the class's constructor (__init__ method), initialized attributes including file_path (path to the text document) and email_pattern (a regular expression pattern to match email addresses).
2. Defined the extract_emails method to extract email addresses from the text document: Opened the text document specified in file_path. Read the document line by line.
3. Used the re.findall function with email_pattern to find all email addresses in each line. Added the extracted email addresses to the emails list.
4. Inside the main block: Created an instance email_extractor of the EmailExtractor class, specifying the path to 'document.txt' as the argument.
5. Called the extract_emails method to extract email addresses and stored them in email_addresses. Printed each extracted email address.

Task 4:
1. Created a class Employee to represent employees with an __init__ method that initializes the employee attribute and a get_info method to return information about all employees.
2. Created a subclass Manager that inherits from Employee. In the Manager class: Implemented an __init__ method that calls the superclass's __init__ method using super() and initializes manager_info. Overridden the get_info method to filter and display information about employees with the "Manager" position.
3. Created another subclass Developer that inherits from Employee. In the Developer class: Implemented an __init__ method that calls the superclass's __init__ method using super() and initializes developer_info. Overridden the get_info method to filter and display information about employees with the "Developer" position.
4. Opened a JSON file ("employee_data.json") and loaded its contents into the data variable.
5. Created an instance mana of the Manager class with the data loaded from the JSON file. Called the get_info method on mana to print information about employees who are Managers.
6. Created an instance deve of the Developer class with the data loaded from the JSON file. Called the get_info method on deve to print information about employees who are Developers.

Task 5a:
1. Created a list of student dictionaries.
2. Made a shallow copy of the list by assigning it to another variable. Changes to the shallow copy affected the original list.
3. Created a deep copy of the original list using copy.deepcopy(). Changes to the deep copy did not affect the original list.
4. Modified and added items to both the shallow copy and deep copy.
5. Observed that changes in the shallow copy affected the original list, while changes in the deep copy did not.

Task 5b:
1. Defined a function display_config(config) to display configuration information. This function iterates through a list and prints its items.
2. Defined the production configuration as a list called production_config containing server names.
3. Displayed the original production configuration using the display_config function.
4. Created a deep copy of the production configuration for testing purposes using copy.deepcopy(production_config).
5. Modified the test configuration by appending 'Test Server 4' to the deep copy.
6. Displayed the test configuration to observe the changes.
7. Confirmed that the original production configuration remains unchanged by displaying it again.
