import pytest
from app.models.user import User
from app.services import revenue_service, user_service
from app.models.revenue import Revenue
import datetime


@pytest.mark.asyncio
async def test_get_revenue_by_id():
    """
    Test retrieving revenue by its ID.
    """
    revenue_id = 1
    result = await revenue_service.get_revenue_by_id(revenue_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == revenue_id


@pytest.mark.asyncio
async def test_get_all_revenues_by_user_id():
    """
    Test retrieving all revenues associated with a user by their ID.
    """
    user_id = 1
    result = await revenue_service.get_all_revenues_by_user_id(user_id)
    assert result is not None
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_create_revenue():
    """
    Test creating a new revenue.
    """
    user_id = 1
    # Create a test user
    test_user = User(
        id=user_id,
        user_name="Test User in revenue",
        password="Tes!1111111111",
        email="testuser@example.com",
        address="testuser address",
        phone="1234567890",
        balance=1000.0,
    )
    await user_service.create_user(test_user)

    # Create a new revenue object
    new_revenue = Revenue(
        id=1,
        user_id=user_id,
        total_revenue=1000.0,
        date=datetime.datetime.now(),
        description_revenue="Test Revenue"
    )

    # Call the create_revenue function
    result = await revenue_service.create_revenue(user_id, new_revenue)
    assert result is not None
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_update_revenue():
    """
    Test updating an existing revenue.
    """
    user_id = 1
    # Create a test user
    test_user = User(
        id=user_id,
        user_name="Test User",
        password="Tes!1111111111",
        email="testuser@example.com",
        address="testuser address",
        phone="1234567890",
        balance=1000.0,
    )
    await user_service.create_user(test_user)

    revenue_id = 1
    # Create an initial revenue
    initial_revenue = Revenue(
        id=revenue_id,
        user_id=user_id,
        total_revenue=1500.0,
        date=datetime.datetime.now(),
        description_revenue="initial_revenue Test Revenue"
    )
    await revenue_service.create_revenue(user_id, initial_revenue)

    # Update the revenue
    updated_revenue = Revenue(
        id=revenue_id,
        user_id=user_id,
        total_revenue=150.0,
        date=datetime.datetime.now(),
        description_revenue="Updated Test Revenue"
    )

    # Call the update_revenue function
    result = await revenue_service.update_revenue(revenue_id, updated_revenue)
    assert result is not None
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_delete_revenue():
    """
    Test deleting a revenue by its ID.
    """
    revenue_id = 1
    # Call the delete_revenue function
    result = await revenue_service.delete_revenue(revenue_id)
    assert result is not None
