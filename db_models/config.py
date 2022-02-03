from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from databaseinfo import sql_server, sql_user, sql_database, sql_password
from datetime import datetime

app = Flask(__name__)
#
# ###############################################################
#
# # Database configurations:
#
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{sql_user}:{sql_password}@{sql_server}/{sql_database}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#
#
# ##############################################################
#
class Users(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    # address = db.Column(db.String(60), nullable=True)
    # phone = db.Column(db.String(10), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False, default=False)

    tokens = db.relationship('Tokens', cascade='delete', backref='targetaccount', lazy=True)
    enrolls = db.relationship('Enrollments', cascade='delete', backref='student', lazy=True)
    userinfos = db.relationship('UserInfos',cascade='delete', backref='user', lazy=True)
    posts = db.relationship('Posts', cascade='delete', backref='author', lazy=True)
    password = db.relationship('Secrets', cascade="delete", backref='pwuser', lazy=True)
    sender = db.relationship('Messages',backref='sender', lazy=True)
    receiver = db.relationship('Messages',backref='receiver', lazy=True)

    def dictify(self):
        return {'uid': self.uid, 'first_name': self.first_name, 'last_name': self.last_name, 'isActive': self.isActive}

    def __repr__(self) -> str:
        return f'{self.uid} - {self.first_name}'

class UserInfos(db.Model):
    uiid = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10), nullable=True, unique=True)
    address = db.Column(db.String(60), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)

class Posts(db.Model):
    n_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now())
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'),nullable=False)

class Faculties(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(50), nullable=False)

    courses = db.relationship('Courses', cascade='delete', backref='courses', lazy=True)


class Courses(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(30), nullable=False)
    course_span = db.Column(db.Integer, nullable=True)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.f_id'), nullable=False)
    enrolls = db.relationship('Enrollments',cascade='delete', backref='enrolls', lazy=True)


class Enrollments(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    batch_year = db.Column(db.Integer)

    course_id = db.Column(db.Integer, db.ForeignKey('courses.c_id', ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid', ondelete='CASCADE'))

    def __repr__(self) -> str:
        return f"{self.e_id} - {self.faculty} - {self.faculty}"


class Messages(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text, nullable=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('users.uid'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.uid'))


class Tokens(db.Model):
    token = db.Column(db.String(30), primary_key=True)
    as_user = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)


class Secrets(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(40), nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)

# After this section, we are writing api and stray function codes
