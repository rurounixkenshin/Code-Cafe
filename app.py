# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html', logo_filename=logo_filename, coffee_mug_filename=coffee_mug_filename)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # Add logic for handling sign-in form submission (to be implemented)
    if request.method == 'POST':
        # Retrieve username and password from the form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Add your authentication logic here (e.g., check credentials against a database)

    return render_template('signin.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Add logic for handling registration form submission (to be implemented)
    if request.method == 'POST':
        # Retrieve username, email, and password from the form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Add your registration logic here (e.g., store user data in a database)

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

# Other routes...

if __name__ == '__main__':
    app.run(debug=True)
