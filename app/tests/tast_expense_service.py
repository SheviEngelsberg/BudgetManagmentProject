
import pytest
from app.services import expense_service
from app.services import user_service
from app.models.expense import Expense
from app.models.user import User
import datetime


@pytest.mark.asyncio
async def test_get_expense_by_id():
    """
    Test retrieving an expense by its ID.
    """
    expense_id = 1
    result = await expense_service.get_expense_by_id(expense_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == expense_id


@pytest.mark.asyncio
async def test_get_all_expenses_by_user_id():
    """
    Test retrieving all expenses associated with a user by their ID.
    """
    user_id = 1
    result = await expense_service.get_all_expenses_by_user_id(user_id)
    assert result is not None
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_create_expense():
    """
    Test creating a new expense.
    """
    user_id = 1
    # Creating a new expense object
    new_expense = Expense(
        id=1,
        user_id=user_id,
        total_expense=100.0,
        date=datetime.now(),
        description_expense="Test Expense"
    )
    # Calling the create_expense function
    result = await expense_service.create_expense(user_id, new_expense)
    assert result is not None
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_update_expense():
    """
    Test updating an existing expense.
    """
    # Step 1: Creating a test user
    user_id = 1
    test_user = User(
        id=user_id,
        user_name="Test User in expense",
        password="Test!7777777",
        email="testuser@example.com",
        address="test_user address",
        phone="1234567890",
        balance=1000.0,
    )
    await user_service.create_user(test_user)

    # Step 2: Creating an initial expense
    expense_id = 1
    initial_expense = Expense(
        id=expense_id,
        user_id=user_id,
        total_expense=50.0,
        date=datetime.now(),
        description_expense="Test Expense initial"
    )
    await expense_service.create_expense(user_id, initial_expense)

    # Step 3: Updating the expense
    updated_expense = User(
        id=expense_id,
        user_id=user_id,
        total_expense=150.0,
        date=datetime.now(),
        description_expense="Test Expense updated"
    )
    # Calling the update_expense function
    result = await expense_service.update_expense(expense_id, updated_expense)
    assert result is not None
    assert isinstance(result, str)


@pytest.mark.asyncio
async def test_delete_expense():
    """
    Test deleting an expense by its ID.
    """
    expense_id = 1
    # Calling the delete_expense function
    result = await expense_service.delete_expense(expense_id)
    assert result is not None
