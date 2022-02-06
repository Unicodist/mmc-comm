from custom.exceptions import *
from db_models.config import *
from flask_restful import abort

def getuserbyuid(uid):
    user = Users.query.filter_by(uid=uid).first()
    if user is None:
        raise DataNotFoundException('Such user doesn\'t exist in the database')
    else:
        return user


def getusersinfobyphone(phone):
    phoneinfo = UserInfos.query.filter_by(phone=phone).first()
    if phoneinfo is None:
        DataNotFoundException('The phone number do not exist in the database')
    else:
        return phoneinfo.user

def abort_if_user_not_found(uid):
    try:
        user = getuserbyuid(uid)
    except DataNotFoundException:
        abort(401,'User doesn\'t exist in the database')
