from flask import Flask, render_template

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# db = SQLAlchemy(app)

posts = [
    {
        'author': 'Souler Tsai',
        'title': 'Blog Post',
        'content': 'First blog content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second blog content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts=posts) 

@app.route('/about')
def about():
    return render_template('about.html', title="About") 

if __name__ == "__main__":
    app.run(debug=True)