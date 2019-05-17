from App.Permission import permission
from App.Permission.controllers import *
from flask import Flask, request, g
from App.decorators import auth, root_requied, permission_requied
from config import ROOT_NAME

@permission.route('/add_permission', methods=['Post'])
@auth.login_required
@root_requied
def add_permission():
    user_id = request.form.get('user_id')
    camera_id = request.form.get('camera_id')
    return 'pass'


@permission.route('/remove_permission', methods=['Post'])
@auth.login_required
@root_requied
def remove_permission():
    user_id = request.form.get('user_id')
    camera_id = request.form.get('camera_id')
    return 'pass'
