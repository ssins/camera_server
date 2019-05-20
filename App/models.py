from flask_sqlalchemy import SQLAlchemy
import datetime
import json

db = SQLAlchemy()
unknown = 'unknown'


# 自定义基类
class base():
    id = db.Column(db.Integer, primary_key=True)
    update_time = db.Column(db.TIMESTAMP, nullable=False)

# 序列化
class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, base):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (
                            datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)


class Camera(db.Model, base):
    sn = db.Column(db.String(255)) #SN号
    address = db.Column(db.String(255))  # 摄像头地址
    action_type = db.Column(db.String(255))  # SDK标识
    user_name = db.Column(db.String(255))  # 摄像头登录名
    password = db.Column(db.String(255))  # 密码
    statues = db.Column(db.String(255))  # 设备状态
    kind = db.Column(db.String(255))  # 种类
    brand = db.Column(db.String(255))  # 品牌
    model = db.Column(db.String(255))  # 型号
    name = db.Column(db.String(255))

    def __init__(self, sn, address, action_type, user_name, password, statues=unknown, kind=unknown, brand=unknown, model=unknown, name=unknown):
        self.sn = sn
        self.address = address
        self.action_type = action_type
        self.user_name = user_name
        self.password = password
        self.statues = statues
        self.kind = kind
        self.brand = brand
        self.model = model
        self.name = name

    def __repr__(self):
        return '<Camera %r - %r>' % (self.name, self.address)


class User(db.Model, base):
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    token = db.Column(db.String(255))
    key = db.Column(db.String(255))

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.user_name


class Permission(db.Model, base):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('permissions', lazy='dynamic'))
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.id'))
    camera = db.relationship(
        'Camera', backref=db.backref('permissions', lazy='dynamic'))

    def __init__(self, user, camera):
        self.user = user
        self.camera = camera

    def __repr__(self):
        return '<Permission %r - %r>' % (self.user.user_name, self.camera.name)
