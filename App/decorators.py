from flask import Flask, request, g
from flask_httpauth import HTTPTokenAuth
from App.models import *
from config import ROOT_NAME
from functools import wraps

auth = HTTPTokenAuth(scheme='Bearer')

# 登录验证装饰器
@auth.verify_token
def verify_token(token):
    if token:
        g.user = User.query.filter_by(token=token).first()
        if g.user:
            return True
    return False

# 管理员操作权限装饰器
def root_requied(fn):
    @wraps(fn)
    def verify_root(*args):
        if g.user and g.user.user_name == ROOT_NAME:
            return fn(*args)
        return 'Permission denied', 500
    return verify_root

# 摄像头操作权限装饰器
def permission_requied(fn):
    @wraps(fn)
    def verify_permission(*args):
        camera_id = request.form.get('camera_id')
        if not camera_id:
            camera_id = request.args.get('camera_id')
        if g.user and camera_id:
            # root用户拥有全部权限
            if g.user.user_name == ROOT_NAME:
                return fn(*args)
            p = Permission.query.filter_by(
                user_id=g.user.id, camera_id=camera_id).first()
            if p:
                return fn(*args)
            return 'Permission denied', 500
        return 'args error', 200
    return verify_permission
