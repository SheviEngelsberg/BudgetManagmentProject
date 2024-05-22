from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    user_id: int
    total_expense: float
    date: datetime
    account_number: str


