"""Flask based app using FLask-SQLAlchemy."""

from flask import Flask
from flask import render_template
# from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# We want to instantiate our db through SQLAlchemy. But this time we will do it
# using flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'  # Creates
# the SQLALCHEMY_DATABASE_URI pointing to our DB file.

# Initialise the DB and set it up in the flask app
db = SQLAlchemy()  # Initialising the db using flask's SQLAlchemy
db.init_app(app)  # Initialising the db app by passing the flask app
app.app_context().push()  # Pushing it to the context

'''
The only difference here is that we import the base model from flask_sqlAlchemy
We will be using db.Model as a parameter to each class we initialise for the
tables.
Each method will now begin with db.*
'''


class USER(db.Model):
    """USER class extends the base class, defined by db.Model."""

    __tablename__ = 'user'  # Same table name as in the db
    # Now, we define the schema of the table. Use the same names as that in the
    # .sqlite3 file
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    # We can define a many-to-one relationship as follows ->
    # articles_relationship = db.relationship("ARTICLE", secondary="authors")


class ARTICLE(db.Model):
    """ARTICLE class extends the base class, defined by db.Model."""

    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    # We need to define many-to-many relationship between users and articles.
    # Whenever I get users, i want articles too
    # In our case, an article can have many users(as authors)
    # Authors linking to user's table through a secondary table called
    # authors
    authors_relationship = db.relationship("USER", secondary="authors")


class AUTHORS(db.Model):
    """AUTHORS class extends the base class, defined by db.Model."""

    __tablename__ = 'authors'
    article_id = db.Column(db.Integer, db.ForeignKey("article.article_id"),
                           primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),
                        primary_key=True, nullable=False)


'''-----------------------Till now we have set up the model -------------------------------'''


@app.route('/', methods=['GET', 'POST'])
def articles():
    articles = ARTICLE.query.all()
    # We can use either of the following methods
    # articles = db.session.query(ARTICLE).all()

    return render_template("articles.html", articles=articles)


@app.route('/articles_by/<user_name>', methods=['GET', 'POST'])
def articles_by(user_name):
    articles = ARTICLE.query.filter(ARTICLE.authors_relationship.any(username=user_name))

    return render_template("articles_by_Auth.html", articles=articles, username=user_name)


app.run(debug=True)
