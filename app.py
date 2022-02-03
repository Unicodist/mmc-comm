import hashlib
from db_models.config import *
from flask_restful import Api, Resource, abort, reqparse
from custom.exceptions import DataNotFoundException

user_put_args = reqparse.RequestParser()
user_put_args.add_argument('firstname', type=str, help='Please input firstname', required=True)
user_put_args.add_argument('lastname', type=str, help='Please input lastname', required=True)
user_put_args.add_argument('address', type=str, help='Please input address', required=True)
user_put_args.add_argument('phone', type=str, help='Please enter phone number', required=True)
user_put_args.add_argument('password', type=str, help='Please choose a password', required=True)

login_post_args = reqparse.RequestParser()
login_post_args.add_argument('phone', type=str, help='Please enter the phone', required=True)
login_post_args.add_argument('password', type=str, help='Please enter password', required=True)

api = Api(app)


# some stray functions here:

def getuserbyuid(uid):
    user = Users.query.filter_by(uid=uid).first()
    if user is None:
        raise DataNotFoundException('Such user doesn\'t exist in the database')
    else:
        return user


def getusersinfobyphone(phone):
    phone = UserInfos.query.filter_by(phone=phone).first()
    if phone is None:
        DataNotFoundException('The phone number do not exist in the database')
    else:
        return phone

def abort_if_user_not_found(uid):
    try:
        user = getuserbyuid(uid)
    except DataNotFoundException:
        abort(401,'User doesn\'t exist in the database')

# def verifyToken(token):
#     if Tokens.query.filter_by(token=token).count() != 0:
#         return abort(409,"Sorry! You are not authorized!")
#     return True
# Api classes:

class UserObject(Resource):
    def get(self, uid):
        try:
            user = getuserbyuid(uid)
        except DataNotFoundException as de:
            abort(402,'The user is not found')
        return jsonify(user.dictify())

    def put(self, uid=None):
        uid = None
        args = user_put_args.parse_args()
        new_user = Users(fname=args['firstname'], lname=args['lastname'])
        db.session.add(new_user)
        moreinfo = UserInfos(phone=args['phone'], address=args['address'], user=new_user)
        db.session.add(moreinfo)
        secret = Secrets(pw=hashlib.md5(args['password'].encode('utf8')).hexdigest(), pwuser=new_user)
        db.session.add(secret)
        db.session.commit()
        return {'status':'success','phone':args['phone']}


class MessageObject(Resource):
    def get(self,sender):
        pass

    def post(self):
        pass

class MessageMenuObject(Resource):
    def get(self):
        pass


class LoginObject(Resource):
    def post(self):
        #stores all the post values in the variable called args
        args = login_post_args.parse_args()
        #retrieves data from Usersinfo table that matches phone
        #if the phone is not found, throws error
        userinfo = getusersinfobyphone(args['phone'])
        target_user = userinfo.user
        print(target_user)


# Api classes end here


# registering api classes:
api.add_resource(UserObject, "/api/user/<int:uid>/")
api.add_resource(MessageObject, '/api/Message/')
api.add_resource(LoginObject, '/api/login/')

# entry point:
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
