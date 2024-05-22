from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services import user_service
import json
from bson import json_util

user_router = APIRouter()

@user_router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        return await user_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.get('')
async def get_all_users():
    try:
        return await user_service.get_all_users()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.post('')
async def add_user(new_user: User):
    try:
        return await user_service.create_user(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.put('')
async def update_user(new_user: User):
    try:
        return await user_service.update_user(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


