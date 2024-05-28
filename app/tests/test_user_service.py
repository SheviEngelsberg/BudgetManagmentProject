import pytest
from app.services import user_service
from app.models.user import User


@pytest.mark.asyncio
async def test_get_user_by_id():
    """
    Test the function to retrieve a user by ID.

    Retrieves a user by their ID and checks if the returned result is not None,
    is a dictionary, and contains the correct user ID.
    """
    user_id = 1
    result = await user_service.get_user_by_id(user_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == user_id


@pytest.mark.asyncio
async def test_add_user():
    """
    Test the function to add a new user.

    Adds a new user to the system and checks if the returned result is not None
    and is a dictionary.
    """
    new_user = User(
        id=1,
        user_name="test_user",
        password="Test1234!",
        email="test@example.com",
        address="123 Test St",
        phone="1234567890",
        balance=0.0
    )
    result = await user_service.create_user(new_user)
    assert result is not None
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_login_user():
    """
    Test the function to login a user.

    Creates a new user, then attempts to login with the same credentials,
    and checks if the returned result is not None, is a list, and has the expected username.
    """
    user_name = "test_user"
    user_password = "Test1234!"
    new_user = User(
        id=1,
        user_name=user_name,
        password=user_password,
        email="test@example.com",
        address="123 Test St",
        phone="1234567890",
        balance=0.0
    )
    await user_service.create_user(new_user)
    result = await user_service.login_user(user_name, user_password)
    assert result is not None
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["user_name"] == user_name


@pytest.mark.asyncio
async def test_update_user():
    """
    Test the function to update a user's information.

    Updates an existing user's information and checks if the returned result is not None
    and is a string.
    """
    user_id = 1
    updated_user = User(
        id=user_id,
        user_name="updated_user_name",
        password="Updated1234!",
        email="updated@example.com",
        address="456 Updated St",
        phone="0987654321",
        balance=100.0
    )
    result = await user_service.update_user(user_id, updated_user)
    assert result is not None
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_delete_user():
    """
    Test the function to delete a user.

    Deletes an existing user from the system and checks if the returned result is not None
    and is a string.
    """
    user_id = 1
    result = await user_service.delete_user(user_id)
    assert result is not None
    assert isinstance(result, str)
