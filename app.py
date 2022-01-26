sql_server = 'localhost'
sql_user = 'root'
sql_password = ''

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

###############################################################

# Database configurations:

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:@localhost/ashura"
# app.config['SQLALCHMY_BINDS'] = {
#     'localdb': f"mysql://{sql_user}:{sql_password}@{sql_server}/ashura"
# }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##############################################################

class Users(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"{self.uid} - {self.name}"

class Courses(db.Model):
    c_id = db.Column(db.Integer,primary_key=True)
    faculty_id = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(30), nullable=False)
    course_span = db.Column(db.Integer,nullable=True)

class Faculties(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(50),nullable=False)

class Enrollment(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.String(50), nullable=False)
    course = db.Column(db.String(30), nullable=False)
    batch_year = db.Column(db.Integer)

    def __repr__(self) ->str:
        return f"{self.e_id} - {self.faculty} - {self.faculty}"


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/loginHandler', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    print(username)
    return "Hello There!"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
