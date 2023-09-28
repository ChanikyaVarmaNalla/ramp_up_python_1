import json
from flask import Flask, request, jsonify, redirect, url_for, session, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key of your choice

# Custom decorator to check if a user is authenticated and authorized
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function

# Load user credentials from credentials.json
def load_credentials():
    try:
        with open('credentials.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

# Save user credentials to credentials.json
def save_credentials(credentials):
    with open('credentials.json', 'w') as json_file:
        json.dump(credentials, json_file, indent=4)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        authorized = request.form.get('authorized')

        # Load existing credentials
        credentials = load_credentials()

        # Check if the username is already taken
        if any(cred['username'] == username for cred in credentials):
            return jsonify({'message': 'Username already exists'})

        # Create a new user dictionary and append it to the credentials list
        new_user = {'username': username, 'password': password, 'authorized': authorized}
        credentials.append(new_user)

        # Save updated credentials to credentials.json
        save_credentials(credentials)

        # Redirect to the login page with a success message
        return redirect(url_for('login', registration_successful=True))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    registration_successful = request.args.get('registration_successful')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Load existing credentials
        credentials = load_credentials()

        # Check if the provided credentials match any user in the credentials list
        user = next((cred for cred in credentials if cred['username'] == username and cred['password'] == password), None)

        if user:
            session['username'] = user['username']  # Store the username in the session
            return redirect(url_for('protected'))

        return jsonify({'message': 'Login failed'})

    return render_template('login.html', registration_successful=registration_successful)

# Protected route that requires authentication and authorization
@app.route('/protected')
@login_required  # Apply the login_required decorator
def protected():
    username = session.get('username')
    credentials = load_credentials()

    # Find the user in the credentials list
    user = next((cred for cred in credentials if cred['username'] == username), None)

    if user and user['authorized'] == 'yes':
        # Load employee data from employee_data.json
        with open('employee_data.json', 'r') as json_file:
            employee_data = json.load(json_file)

        return render_template('message.html', employee_data=employee_data['employees'], message="Logged in with Authorized Credentials")
    else:
        return jsonify({'message': 'Login successful but not authorized'})


if __name__ == '__main__':
    app.run(debug=True)
