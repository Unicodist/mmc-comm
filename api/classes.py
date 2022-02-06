from flask_restful import Resource
from api.functions import *
from flask import jsonify
from custom.request_parser import *
import hashlib
from sqlalchemy.exc import IntegrityError

class UserObject(Resource):
    def get(self, uid):
        try:
            user = getuserbyuid(uid)
        except DataNotFoundException as de:
            abort(402, 'The user is not found')
        return jsonify(user.dictify())

    def put(self, uid=None):
        uid = None
        args = user_put_args.parse_args()
        try:
            new_user = Users(first_name=args['firstname'], last_name=args['lastname'])
            db.session.add(new_user)
            moreinfo = UserInfos(phone=args['phone'], address=args['address'], user=new_user)
            db.session.add(moreinfo)
            secret = Secrets(pw=hashlib.md5(args['password'].encode('utf8')).hexdigest(), pwuser=new_user)
            db.session.add(secret)
            db.session.commit()
            return {'status': 'success', 'phone': args['phone']}
        except IntegrityError as ie:
            return {'status':'failed','message':'Phone number is already registered'}


class MessageObject(Resource):
    def get(self, sender):
        pass

    def post(self):
        pass


class MessageMenuObject(Resource):
    def get(self):
        pass


class LoginObject(Resource):
    def post(self):
        args = login_post_args.parse_args()
        phone = args['phone']
        password = args['password']
        print(phone,password)
        try:
            user = getusersinfobyphone(phone)
            print(user)
        except DataNotFoundException as de:
            return de

api.add_resource(UserObject, "/api/user/<int:uid>/")
api.add_resource(MessageObject, '/api/Message/')
api.add_resource(LoginObject, '/api/login/')
