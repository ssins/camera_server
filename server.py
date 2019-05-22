from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG, ROOT_NAME
from flask import redirect, url_for
from App import create_app
from App.models import *

app, db = create_app()


@app.route('/')
def root():
    return redirect(url_for('index.root'))

# 初始化数据库
@app.route('/init')
def init():
    try:
        db.drop_all()
        db.create_all()
        # 初始化root用户
        root = User(ROOT_NAME, ROOT_NAME)
        db.session.add(root)
        db.session.commit()
    except:
        return 'fail'
    return 'success'


# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, 'dpe:', ['env='])
#     except getopt.GetoptError:
#         print 'server.py -e <dev or pro>'
#         sys.exit(2)
#     for opt, arg in opts:
#       if opt == '-p':
#          print 'test.py -i <inputfile> -o <outputfile>'
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg

if __name__ == '__main__':
    # main(sys.argv[1:])
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
