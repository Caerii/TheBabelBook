from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)

    # Configure the database URI and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy object and bind it to the Flask application
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    __tablename__ = 'User'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50), nullable=False)
    UserPassword = db.Column(db.String(50), nullable=False)
    OpenAIKey = db.Column(db.String(50), nullable=False)

# Define the Session model
class Session(db.Model):
    __tablename__ = 'Session'
    SessionID = db.Column(db.Integer, primary_key=True)
    SessionDate = db.Column(db.String(50), nullable=False)
    Book = db.Column(db.Integer, nullable=False)
    ShareLink = db.Column(db.String(50), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), nullable=False)

# Define the Book model
class Book(db.Model):
    __tablename__ = 'Book'
    BookID = db.Column(db.Integer, primary_key=True)
    AuthorName = db.Column(db.String(50), nullable=False)
    ChapterID = db.Column(db.Integer, nullable=False)
    BookTitle = db.Column(db.String(50), nullable=False)
    BookDescription = db.Column(db.String(255), nullable=False)
    BookCreationDate = db.Column(db.String(50), nullable=False)
    ShareLink = db.Column(db.String(50), nullable=False)
    SessionID = db.Column(db.Integer, db.ForeignKey('Session.SessionID'), nullable=False)

# Define the Chapter model
class Chapter(db.Model):
    print('Chapter')
    __tablename__ = 'Chapter'
    ChapterID = db.Column(db.Integer, primary_key=True)
    ChapterHeader = db.Column(db.String(50), nullable=False)
    ChapterText = db.Column(db.String(255), nullable=False)
    ChapterComments = db.Column(db.String(255), nullable=False)
    BookID = db.Column(db.Integer, db.ForeignKey('Book.BookID'), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), nullable=False)

# Create the tables in the database
db.create_all()