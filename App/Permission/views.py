from App.Permission import permission
from App.Permission.controllers import *
from flask import Flask, request, g
from App.decorators import auth, root_requied, permission_requied
from config import ROOT_NAME


@permission.route('/add', methods=['Post'])
@auth.login_required
@root_requied
def add():
    user_id = request.form.get('user_id')
    camera_id = request.form.get('camera_id')
    if user_id and camera_id:
        return add_permission(user_id, camera_id)
    return 'args error', 400


@permission.route('/remove', methods=['Post'])
@auth.login_required
@root_requied
def remove():
    user_id = request.form.get('user_id')
    camera_id = request.form.get('camera_id')
    if user_id and camera_id:
        return remove_permission(user_id, camera_id)
    return 'args error', 400
