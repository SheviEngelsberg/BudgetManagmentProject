from fastapi import HTTPException
from app.models.user import User
from app.db.db_functions import get_by_id, get_all
import re


def is_valid_email(email: str) -> bool:
    """
    Check if the input string is a valid email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


async def validate_email_dependency(new_user: User) -> bool:
    """
    Validate the email address of a new user.

    Args:
        new_user (User): The user object with the email to validate.

    Returns:
        bool: True if the email is valid, otherwise raises an HTTPException with status code 400.
    """
    if not is_valid_email(new_user.email):
        raise HTTPException(status_code=400, detail="The email is invalid")
    return True


def is_valid_password(password: str):
    """
    Check if a password meets certain criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character

    Args:
        password (str): The password to validate.

    Raises:
        ValueError: If the password does not meet the specified criteria.

    Returns:
        bool: True if the password is valid, otherwise False.
    """
    if len(password) < 8:
        raise ValueError('password must be at least 8 characters long')
    if not re.search(r'[A-Z]', password):
        raise ValueError('password must contain at least one uppercase letter')
    if not re.search(r'[a-z]', password):
        raise ValueError('password must contain at least one lowercase letter')
    if not re.search(r'[0-9]', password):
        raise ValueError('password must contain at least one number')
    if not re.search(r'[!@#\$%\^&\*]', password):
        raise ValueError('password must contain at least one special character')
    return True


async def validate_password_dependency(new_user: User) -> bool:
    """
    Validate the password of a new user.

    Args:
        new_user (User): The user object with the password to validate.

    Returns:
        bool: True if the password is valid, otherwise raises an HTTPException with status code 400.
    """
    try:
        if is_valid_password(new_user.password):
            return True
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



def is_valid_phone_number(phone_number: str) -> bool:
    """
    Check if the input string is a valid phone number.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    if len(phone_number) < 9 or len(phone_number) > 10:
        return False
    if not phone_number.isdigit():
        return False
    return True


async def validate_phone_dependency(new_user: User) -> bool:
    """
    Validate the phone number of a new user.

    Args:
        new_user (User): The user object with the phone number to validate.

    Returns:
        bool: True if the phone number is valid, otherwise raises an HTTPException with status code 400.
    """
    if not is_valid_phone_number(new_user.phone):
        raise HTTPException(status_code=400, detail="The phone number is incorrect. Phone should contain 9-10 digits")
    return True


def is_valid_expense(amount: int) -> bool:
    """
    Check if the input integer is a valid expense amount.

    Args:
        amount (int): The amount to validate.

    Returns:
        bool: True if the amount is valid, False otherwise.
    """
    if amount < -100000:
        return False
    return True


async def validate_expense_dependency(user_id: int) -> bool:
    """
    Validate the expense amount of a user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        bool: True if the expense is valid, otherwise raises an HTTPException with status code 400.
    """
    user = await get_by_id(user_id, "users")
    if not is_valid_expense(user['balance']):
        raise HTTPException(status_code=400, detail="The expense is too great, it is not possible to enter a deficit of more than $100,000")
    return True


async def is_valid_username(username: str) -> bool:
    """
    Check if the input string is a valid username.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    if not username.isalpha():
        return False
    if await username_exists_in_database(username):
        return False
    return True


async def username_exists_in_database(username: str) -> bool:
    """
    Check if a username exists in the database.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the username exists in the database, False otherwise.
    """
    users = await get_all("users")
    if not users:
        return False
    for user in users:
        if user['user_name'] == username:
            return True
    return False


async def validate_user_name_dependency(new_user: User) -> bool:
    """
    Validate the username of a new user.

    Args:
        new_user (User): The user object with the username to validate.

    Returns:
        bool: True if the username is valid, otherwise raises an HTTPException with status code 400.
    """
    is_username_valid = await is_valid_username(new_user.user_name)
    if not is_username_valid:
        raise HTTPException(status_code=400, detail="The username already exists in the system")
    return True
