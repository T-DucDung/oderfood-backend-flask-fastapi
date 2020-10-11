from models import users_model

def get_user(user_id: int):
    print("hihi")
    print(user_id)
    return users_model.select_user_by_id(user_id)
