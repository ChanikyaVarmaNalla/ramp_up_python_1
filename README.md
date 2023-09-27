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

Task 6:
1. Created a UserProfile class to manage user profiles. An instance of this class was initialized with a username, email, and age.
2. Retrieved the existing profile data using the get_profile method and stored it in the old_profile variable. This data was then displayed on the screen.
3. Updated user profile details by modifying user information, which included changing the email and age, and adding extra details such as "city" and "hobbies."
4. The update_profile method was applied to update the user's profile using the information from new_data. This method handled email and age updates separately and merged any additional data into the profile.
5. Obtained the updated profile data using the get_profile method and stored it in the updated_profile variable. The updated profile information was subsequently displayed on the screen.

Task 7:
1. An instance of the BlogPostCMS class is created, setting up the content management system. The code checks for the existence of a "blog_posts" directory; if it doesn't exist, the code creates it to store blog posts.
2. User input is collected for the title and content of a new blog post. The code verifies if a blog post with the same title already exists in the "blog_posts" directory.
3. If the same-title blog post exists, the code notifies the user; otherwise, a new blog post file is generated with the provided title and content.
4. User input is received for the title of the blog post they wish to read. The code checks for the existence of a blog post with the given title.
5. If the blog post exists, its content is read from the file and displayed; otherwise, the user is informed that the post is not found.
6. User input is taken for the title of the blog post they want to edit. If the blog post exists, its current content is displayed, and the user can enter new content. The new content overwrites the previous content, and a success message is shown. If it doesn't exist, a message informs the user that the blog post isn't found.

Task 8:
1. Created a Flask application (app.py) with Flask and Flask-SocketIO. Defined routes /user1 and /user2 for two users and socket events (join and text) for real-time chat. Set up the app to handle user connections, message broadcasting, and message reception.
2. Created an HTML template (user1.html) for User 1's chat interface. Included necessary JavaScript libraries for Socket.IO and jQuery. Set up the template to connect to the chat server, display messages, and send messages as User 1.
3. Created an HTML template (user2.html) for User 2's chat interface. Included necessary JavaScript libraries for Socket.IO and jQuery. Set up the template to connect to the chat server, display messages, and send messages as User 2.
4. In this final step, we run the Flask application using the socketio.run(app, debug=True) line. This started the Flask development server along with Socket.IO, allowing real-time communication.
