sql_server = 'localhost'
sql_user = 'root'
sql_password = ''

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

###############################################################

#Database configurations:

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////databases/test.db"
app.config['SQLALCHMY_BINDS'] = {
    'localdb':"mysql://root:@localhost/ashura"
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##############################################################

##############################################################

#Any functions for general use is defined within this area.

##############################################################

class users(db.Model):
    __bind_key__ = 'localdb'
    uid = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20),nullable=False)

    def __repr__(self) -> str:
        return f"{self.uid} - {self.name}"

class enrollment:
    __bind_key__ = 'localdb'
    faculty = db.Column(db.String(50),nullable=False)
    course = db.Column(db.String(30),nullable=False)
    batch_year = db.Column(db.Integer)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/loginHandler', methods = ['GET','POST'])
def login():
    username = request.form['username']
    print(username)
    return "Hello There!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)