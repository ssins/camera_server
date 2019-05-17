import os
BASE_DIR = os.getcwd()

# flask server
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 3333
FLASK_DEBUG = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1qaz2wsx@localhost:3306/camera'
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# root user name
# change the database value if you changed this value
ROOT_NAME = 'root'