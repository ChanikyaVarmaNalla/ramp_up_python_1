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
