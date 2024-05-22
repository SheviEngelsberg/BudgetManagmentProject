from fastapi import APIRouter, HTTPException
from app.models.expenses import Expenses
from app.services import expenses_service
import json
from bson import json_util

expenses_router = APIRouter()


@expenses_router.get('/login/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        return await expenses_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expenses_router.get('')
async def get_all_users():
    try:
        return await user_service.get_all_users()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expenses_router.post('/create')
async def create_expenses(new_expenses: Expenses):
    try:
        return await expenses_service.create_expenses(new_expenses)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expenses_router.put('/profile_update/{user_id}')
async def update_user(user_id: int, new_user: User):
    try:
        return await user_service.update_user(user_id, new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



