# app.py
from flask import Flask, redirect, render_template, request, session, url_for
from psutil import users

app = Flask(__name__)

app.secret_key = 'UKHIYE'

registered_users = []


# Sample data for blog posts
blog_posts = [
    {"username": "JohnDoe", "date": "2023-12-01", "time": "14:30", "topic": "Python", "description": "Introduction to Python Programming."},
    {"username": "JaneSmith", "date": "2023-12-02", "time": "10:45", "topic": "Web Development", "description": "Building responsive websites with HTML, CSS, and JavaScript."},
]

# Sample data for projects
projects_data = [
    {"name": "Project 1", "description": "Description of Project 1"},
    {"name": "Project 2", "description": "Description of Project 2"},
]

# Social links
social_links = {
    "twitter": "https://twitter.com/your_twitter",
    "linkedin": "https://linkedin.com/in/your_linkedin",
    "github": "https://github.com/your_github",
}

# Image filenames
logo_filename = "images/Code Cafe Logo.png"  # Adjust the filename accordingly
coffee_mug_filename = "images/Code Cafe Logo.png"  # Adjust the filename accordingly

# Sample user data (replace with a database in a real application)
users = {
    'john_doe': {'password': 'password123'},
    'jane_smith': {'password': 'secret'},
}

@app.route('/')
def home():
    show_buttons = 'username' not in session
    return render_template('home.html', logo_filename=logo_filename, coffee_mug_filename=coffee_mug_filename, show_buttons=show_buttons)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the provided username exists and the password is correct
        user = next((user for user in registered_users if user['username'] == username and user['password'] == password), None)

        if user:
            # Set the session username to the signed-in user
            session['username'] = username
            return redirect(url_for('home'))

        # If the username or password is incorrect, show an error message
        error_message = 'Invalid username or password'

    return render_template('signin.html', error_message=error_message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user details from the registration form
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Perform registration logic (add user to the list, validate inputs, etc.)
        # In a real application, you would hash the password and store it securely

        # For this example, let's assume registration is successful
        registered_users.append({'username': username, 'email': email, 'password': password})

        # Set the session username to the registered user
        session['username'] = username

        # Redirect the user to their profile page
        return redirect(url_for('user_profile'))

    # Render the registration template for the 'GET' request
    return render_template('register.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/project_details/<project_name>')
def project_details(project_name):
    # Add logic to fetch project details based on the project_name
    # This could involve querying a database or fetching data from another source
    # For now, let's just display a simple message
    return f"Details for {project_name}"

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog_post_details/<post_date>/<post_topic>')
def blog_post_details(post_date, post_topic):
    # Add logic to fetch blog post details based on the post_date and post_topic
    # This could involve querying a database or fetching data from another source
    # For now, let's just display a simple message
    return f"Details for the blog post on {post_date} with the topic {post_topic}"

@app.route('/about')
def about():
    return render_template('about.html', social_links=social_links)

@app.route('/profile')
def profile():
    # Get the current session username
    username = session.get('username', None)

    # Fetch user data based on the username
    user = next((user for user in registered_users if user['username'] == username), None)

    return render_template('profile.html', user=user)

@app.route('/user_profile')
def user_profile():
    # Your logic to fetch user data
    user_data = {'username': 'JohnDoe', 'email': 'john@example.com', 'bio': 'A passionate coder.'}
    return render_template('profile.html', user_data=user_data)


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # Get the current user's username from the session
    username = session.get('username')

    # Fetch user data from the users dictionary
    user_data = users.get(username, {})

    if request.method == 'POST':
        # Update user data based on the form submission
        user_data['password'] = request.form.get('password')
        user_data['email'] = request.form.get('email')
        user_data['bio'] = request.form.get('bio')

        # Add more fields as needed (e.g., social links, profile image)

        # Save the updated user data (in a real application, update the database)
        users[username] = user_data

        # Redirect the user to their updated profile page
        return redirect(url_for('user_profile'))

    return render_template('edit_profile.html', user_data=user_data)

@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

# ... (your existing code)

if __name__ == '__main__':
    app.run(debug=True)

# Other routes...

if __name__ == '__main__':
    app.run(debug=True)
