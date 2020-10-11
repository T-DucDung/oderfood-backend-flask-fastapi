from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text
from models.model_global import db, ma

class User(db.Model):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    content = Column(String(50))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
        # load_instance = True

def select_user_by_id(user_id) -> dict:
    """

    :param user_id:
    :return:
    """
    user_schema = UserSchema()
    print(user_id)
    print(type(user_id))
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return send_abort(message=f"user with user_id: {user_id} not exist", code=HTTP_404_NOT_FOUND)
    data = user_schema.dump(user)
    return data
