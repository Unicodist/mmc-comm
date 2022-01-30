from flask import Flask, jsonify
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy
from databaseinfo import sql_server, sql_user, sql_database, sql_password

app = Flask(__name__)
api = Api(app)
#
# ###############################################################
#
# # Database configurations:
#
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{sql_user}:{sql_password}@{sql_server}/{sql_database}"
app.config['SQLALCHMY_BINDS'] = {
    'localdb': f"mysql://{sql_user}:{sql_password}@{sql_server}/ashura"
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#
#
# ##############################################################
#
class Users(db.Model):

    def __init__(self, fname, lname, address, phone):
        self.first_name = fname
        self.last_name = lname
        self.address = address
        self.phone = phone
        self.isActive = True

    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(60), nullable=True)
    phone = db.Column(db.String(10), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"{self.uid} - {self.name}"


class Courses(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(30), nullable=False)
    course_span = db.Column(db.Integer, nullable=True)


class Faculties(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(50), nullable=False)


class Enrollment(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.String(50), nullable=False)
    course = db.Column(db.String(30), nullable=False)
    batch_year = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.e_id} - {self.faculty} - {self.faculty}"


# After this section, we are writing api codes
# some stray functions here:

def abort_if_user_not_found(uid):
    if Users.query.filter_by(uid=uid).count() == 0:
        abort(409, message="User not registered")


# Api classes:

class UsersApi(Resource):
    def get(self, fname, lname, phone, address):
        data = {
            'fname':fname,
            'lname':lname,
            'phone':phone,
            'address':address
        }
        abort_if_user_not_found()
        # return Users.query.filter_by(uid=user_id).first()
        return jsonify(data)

    def put(self, fname, lname, phone, address):
        print(fname,lname,phone,address)
        regUser = Users(fname, lname, address, phone)
        Users.add(regUser)
        Users.commit()


# Api classes end here


# registering api classes:
api.add_resource(UsersApi, "/api/user/<string:fname>")

# entry point:
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
