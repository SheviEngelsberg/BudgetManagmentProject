from app.models.expenses import Expenses


async def create_expenses(new_expenses: Expenses):
    try:
        return await db_functions.add(new_expenses, collection_name="expenses")
    except Exception as e:
        # Raising an exception if one occurs
        raise e
