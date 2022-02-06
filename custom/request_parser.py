from flask_restful import reqparse

user_put_args = reqparse.RequestParser()
user_put_args.add_argument('firstname', type=str, help='Please input firstname', required=True)
user_put_args.add_argument('lastname', type=str, help='Please input lastname', required=True)
user_put_args.add_argument('address', type=str, help='Please input address', required=True)
user_put_args.add_argument('phone', type=str, help='Please enter phone number', required=True)
user_put_args.add_argument('password', type=str, help='Please choose a password', required=True)

login_post_args = reqparse.RequestParser()
login_post_args.add_argument('phone', type=str, help='Please enter the phone', required=True)
login_post_args.add_argument('password', type=str, help='Please enter password', required=True)
