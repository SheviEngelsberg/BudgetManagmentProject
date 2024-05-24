import bcrypt
from app.db import db_functions
from app.models.user import User


async def get_all_users():
    """
    Retrieves all users.

    Returns:
        list: A list containing dictionaries of user information.
    """
    try:
        return await db_functions.get_all(collection_name="users")
    except Exception as e:
        raise e


async def get_user_by_id(user_id):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's information.
    """
    try:
        user = await db_functions.get_by_id(user_id, collection_name="users")
        if user is None:
            raise ValueError("User not found")
        return user
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_user(new_user: User):
    """
    Creates a new user.

    Args:
        new_user (User): The user object to be created.

    Returns:
        dict: A dictionary containing the result of adding the user.
    """
    try:
        hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())

        new_user.id = await db_functions.last_id(collection_name="users") + 1
        new_user.balance = 0.0
        new_user.password = hashed_password.decode('utf-8')  # Store the hashed password

        user = new_user.dict()
        return await db_functions.add(user, collection_name="users")
    except Exception as e:
        raise e


async def login_user(user_name, user_password):
    """
    Logs in a user.

    Args:
        user_name (str): The username of the user.
        user_password (str): The password of the user.

    Returns:
        list: A list of dictionaries containing user information.
    """
    try:
        all_users = await db_functions.get_all("users")
        for user in all_users:
            if user['user_name'] == user_name and bcrypt.checkpw(user_password.encode('utf-8'), user['password'].encode('utf-8')):
                return [user]
        raise ValueError("User not found or invalid password")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error during login: {e}")


async def update_user(user_id: int, new_user: User):
    """
    Updates a user's profile.

    Args:
        user_id (int): The ID of the user to update.
        new_user (User): The updated user object.

    Returns:
        str: A message indicating the success of the update.
    """
    try:
        existing_user = await get_user_by_id(user_id)
        new_user.balance = existing_user['balance']
        new_user.id = user_id
        user = new_user.dict()
        return await db_functions.update(user, collection_name="users")
    except Exception as e:
        raise e


