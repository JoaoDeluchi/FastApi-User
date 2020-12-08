from typing import List, Dict, Any
from domain.user.schemas import User
from config.db import session, save, commit
UserInterface = Dict[Any, Any]

def get_all() -> List[UserInterface]:
    return [user.serializer() for user in session.query(User)]

def get_by_id( user_id: int) -> UserInterface:
    return session.query(User).filter(user_id == User.id).first().serializer()

def create_user(new_user: UserInterface) -> UserInterface:
    new_user["is_active"] = True
    new_user["is_admin"] = False
    save(User(**new_user))
    return new_user


def turn_admin(user_id):
    user = get_by_id(user_id)
    print(f'User before change status {user["is_admin"]}')
    user['is_admin'] = False if user['is_admin'] == True else True
    print(f'User after change status {user["is_admin"]}')
    commit()
    return 'ok', 200

def delete_user(user_id: int) -> UserInterface:
    user = get_by_id(user_id)
    user['is_active'] = False
    commit()
    return 'ok', 200
