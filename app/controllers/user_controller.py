from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.services import user_service
from app import validators


user_router = APIRouter()


@user_router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's information.
    """
    try:
        return await user_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.get('')
async def get_all_users():
    """
    Retrieves all users.

    Returns:
        list: A list containing dictionaries of user information.
    """
    try:
        users = await user_service.get_all_users()
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.post('/register')
async def add_user(new_user: User,
                   validate_password: bool = Depends(validators.validate_password_dependency),
                   validate_phone: bool = Depends(validators.validate_phone_dependency),
                   validate_user_name: bool = Depends(validators.validate_user_name_dependency),
                   validate_email: bool = Depends(validators.validate_email_dependency)):
    """
    Adds a new user to the system.

    Args:
        new_user (User): The user object to be added.

    Returns:
        dict: A dictionary containing the result of adding the user.
        :param validate_email:
        :param validate_user_name:
        :param validate_phone:
        :param validate_password:
        :param new_user:
    """
    try:
        if validate_password and validate_phone and validate_user_name and validate_email:
            return await user_service.create_user(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.post('/login')
async def login_user(user_name: str, user_password: str):
    """
    Logs in a user.

    Args:
        user_name (str): The username of the user.
        user_password (str): The password of the user.

    Returns:
        list: A list of dictionaries containing user information.
    """

    try:
        return await user_service.login_user(user_name, user_password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.put('/profile_update/{user_id}')
async def update_user(user_id: int, new_user: User,
                      validate_password: bool = Depends(validators.validate_password_dependency),
                      validate_phone: bool = Depends(validators.validate_phone_dependency),
                      validate_user_name: bool = Depends(validators.validate_user_name_dependency),
                      validate_email: bool = Depends(validators.validate_email_dependency)):
    """
    Updates a user's profile.

    Args:
        user_id (int): The ID of the user to update.
        new_user (User): The updated user object.

    Returns:
        str: A message indicating the success of the update.
        :param validate_email:
        :param validate_user_name:
        :param validate_phone:
        :param validate_password:
        :param user_id:
        :param new_user:
    """
    try:
        if validate_password and validate_phone and validate_user_name and validate_email:
            return await user_service.update_user(user_id, new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.delete('/{user_id}')
async def delete_user(user_id: int):
    """
    Deletes a user from the system.

    Args:
        user_id (int): The ID of the user to be deleted.

    Returns:
        dict: A dictionary containing the result of deleting the user.
    """
    try:
        return await user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


