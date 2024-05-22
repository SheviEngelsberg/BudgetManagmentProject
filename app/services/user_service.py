from fastapi import HTTPException

from app.db import db_functions
from app.models.user import User


async def get_all_users():
    try:
        return await db_functions.get_all(collection_name="users")
    except Exception as e:
        raise e


async def get_user_by_id(user_id):
    try:
         return await db_functions.get_by_id(user_id, collection_name="users")
    except Exception as e:
         raise e

async def create_user(new_user: User):
    try:
        existing_user = await get_user_by_id(new_user.id)
        if existing_user:
            raise ValueError("User already exists")
        new_user.balance = 0.0
        user = new_user.dict()
        # Adding the user to the database using the appropriate function from the db_functions module
        return await db_functions.add(user, collection_name="users")
    except Exception as e:
        # Raising an exception if one occurs
        raise e


async def login_user(user_name, user_password):
    try:
       return await db_functions.login("users", user_name, user_password)
    except Exception as e:
        raise e


async def update_user(user_id: int, new_user: User):
    try:
        existing_user = await get_user_by_id(user_id)
        if existing_user is None:
            raise ValueError("User not exists")
        new_user.balance = existing_user['balance']
        new_user.id = user_id
        user = new_user.dict()
        return await db_functions.update(user, collection_name="users")
    except Exception as e:
        raise e
