from App.Camera import camera
from flask import Flask, request, g
from App.models import unknown
from App.Camera.controllers import *
from App.decorators import root_requied, permission_requied, auth


@camera.route('/add', methods=['Post'])
@root_requied
def add():
    address = request.form.get('address')
    action_type = request.form.get('action_type')
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    statues = request.form.get('statues', unknown)
    kind = request.form.get('kind', unknown)
    brand = request.form.get('brand', unknown)
    model = request.form.get('model', unknown)
    name = request.form.get('name', unknown)
    if address and action_type and user_name and password:
        return add_camera(address, action_type, user_name, password, statues, kind, brand, model, name)
    return 'args error', 400


@camera.route('/delete', methods=['Post'])
@root_requied
def delete():
    address = request.form.get('address')
    if address:
        return delete_camera(address)
    return 'args error', 400


@camera.route('/list', methods=['Post', 'Get'])
@auth.login_required
def getlist():
    return list_camera()
