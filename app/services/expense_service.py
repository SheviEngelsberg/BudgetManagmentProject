from app.db import db_functions
from app.models.expense import Expense
from datetime import datetime
from app.services.user_service import update_user
from app.models.user import User


async def get_expense_by_id(expense_id: int):
    try:
        expense = await db_functions.get_by_id(expense_id, collection_name="expenses")
        if expense is None:
            raise ValueError("Expense not found")
        return expense
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_all_expenses_by_user_id(user_id: int):
    try:
        all_expenses = await db_functions.get_all_by_user_id(user_id, collection_name="expenses")
        if not all_expenses:
            raise ValueError("Expenses not found")
        return all_expenses
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_expense(user_id, new_expense: Expense):
    try:
        new_expense.id = await db_functions.last_id(collection_name="expenses") + 1
        new_expense.user_id = user_id
        user = await db_functions.get_by_id(user_id, collection_name="users")
        if user is None:
            raise ValueError("User not found")
        user['balance'] -= new_expense.total_expense
        await db_functions.update(user, collection_name="users")

        new_expense_dict = new_expense.dict()
        return await db_functions.add(new_expense_dict, collection_name="expenses")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def update_expense(expense_id: int, new_expense: Expense):
    try:
        existing_expense = await get_expense_by_id(expense_id)
        last_user_id = existing_expense['user_id']
        last_total_expense = existing_expense['total_expense']

        user_data = await db_functions.get_by_id(last_user_id, "users")
        user = User(**user_data)
        user.balance += last_total_expense
        await update_user(last_user_id, user, True)

        new_user_data = await db_functions.get_by_id(new_expense.user_id, "users")
        new_user = User(**new_user_data)
        new_user.balance -= new_expense.total_expense
        await update_user(new_expense.user_id, new_user, True)

        new_expense.id = new_expense
        new_expense.date = datetime.now()
        updated_expense = new_expense.dict()
        return await db_functions.update(updated_expense, collection_name="expenses")
    except Exception as e:
        raise e


async def delete_expense(expense_id):
    try:
        await db_functions.delete(expense_id, collection_name="expenses")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e
