from App.Permission import static_folder
from App.models import Permission, User, Camera, db


def add_permission(user_id, camera_id):
    per = Permission.query.filter_by(
        user_id=user_id, camera_id=camera_id).first()
    user = User.query.get(user_id)
    camera = Camera.query.get(camera_id)
    if not per and user and camera:
        per = Permission(user, camera)
        db.session.add(per)
        db.session.commit()
        return 'success'
    return 'Permission exist or args error', 400


def remove_permission(user_id, camera_id):
    per = Permission.query.filter_by(
        user_id=user_id, camera_id=camera_id).first()
    if per:
        db.session.delete(per)
        db.session.commit()
        return 'success'
    return 'Permission not exist', 400
