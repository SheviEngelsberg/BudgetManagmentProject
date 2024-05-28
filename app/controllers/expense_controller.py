from fastapi import APIRouter, HTTPException, Depends
from app.models.expense import Expense
from app.services import expense_service
from app import validators

expense_router = APIRouter()


@expense_router.get('/{expense_id}')
async def get_expense_by_id(expense_id: int):
    """
    Retrieve an expense by its ID.

    Args:
        expense_id (int): The ID of the expense to retrieve.

    Returns:
        Expense: The retrieved expense.

    Raises:
        HTTPException: If an error occurs during the retrieval process.
    """
    try:
        return await expense_service.get_expense_by_id(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.get('/user/{user_id}')
async def get_all_expenses_by_user_id(user_id: int):
    """
    Retrieve all expenses belonging to a specific user by their ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        List[Expense]: A list containing all expenses associated with the user.

    Raises:
        HTTPException: If an error occurs during the retrieval process.
    """
    try:
        return await expense_service.get_all_expenses_by_user_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.post('/create_expense_to_user/{user_id}')
async def create_expense_to_user(user_id: int, new_expense: Expense,
                                 validate_expense: bool = Depends(validators.validate_expense_dependency)):
    """
    Create an expense for a specific user.

    Args:
        user_id (int): The ID of the user.
        new_expense (Expense): The expense object to create.

    Returns:
        Expense: The created expense.

    Raises:
        HTTPException: If an error occurs during the creation process.
        :param validate_expense:
        :param user_id:
        :param new_expense:
    """
    try:
        if validate_expense:
            return await expense_service.create_expense(user_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.put('/update_expense/{expense_id}')
async def update_expense(expense_id: int, new_expense: Expense, validate_expense: bool = Depends(validators.validate_expense_dependency)):
    """
    Update an existing expense.

    Args:
        expense_id (int): The ID of the expense to update.
        new_expense (Expense): The updated expense object.

    Returns:
        Expense: The updated expense.

    Raises:
        HTTPException: If an error occurs during the update process.
        :param expense_id:
        :param new_expense:
        :param validate_expense:
    """
    try:
        if validate_expense:
            return await expense_service.update_expense(expense_id, new_expense)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.delete('/delete_expense/{expense_id}')
async def delete_expense(expense_id: int):
    """
    Delete an expense by its ID.

    Args:
        expense_id (int): The ID of the expense to delete.

    Returns:
        str: A message indicating the success of the deletion.

    Raises:
        HTTPException: If an error occurs during the deletion process.
    """
    try:
        return await expense_service.delete_expense(expense_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
