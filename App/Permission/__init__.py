import os
from flask import Blueprint
from config import BASE_DIR

permission = Blueprint('permission', __name__, 
                template_folder=os.path.join(BASE_DIR,'App/Permission/template'),
                static_folder=os.path.join(BASE_DIR,'App/Permission/static'))
static_folder = os.path.join(BASE_DIR,'App/Permission/static')

from App.Permission import views
