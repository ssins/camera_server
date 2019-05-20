from App.Camera import static_folder
from App.models import db, Camera, Permission
from flask import g
from config import ROOT_NAME
import json
from App.models import AlchemyJsonEncoder

def add_camera(sn, address, action_type, user_name, password, statues, kind, brand, model, name):
    camera = Camera.query.filter_by(sn=sn).first()
    if not camera:
        camera = Camera(sn, address, action_type, user_name,
                        password, statues, kind, brand, model, name)
        db.session.add(camera)
        db.session.commit()
        return 'success'
    return 'sn exist', 401


def delete_camera(sn):
    camera = Camera.query.filter_by(sn=sn).first()
    if camera:
        for per in camera.permissions:
            db.session.delete(per)
        db.session.delete(camera)
        db.session.commit()
        return 'success'
    return 'sn not exist', 401


def list_camera():
    if g.user.user_name == ROOT_NAME:
        cameras = Camera.query.all()
    else:
        permissions = g.user.permissions
        cameras = []
        for per in permissions:
            cameras.append(per.camera)
    return json.dumps(cameras, cls=AlchemyJsonEncoder)

