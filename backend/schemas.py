from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReviewCreate(BaseModel):
    contact_number: str
    user_name: str
    product_name: str
    product_review: Optional[str] = None


class ReviewResponse(BaseModel):
    id: int
    contact_number: str
    user_name: str
    product_name: str
    product_review: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
