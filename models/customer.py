from pydantic import BaseModel, EmailStr, Field, ValidationError
from datetime import datetime

# Pydantic model for customer
class Customer(BaseModel):
    unit_number: str
    first_name: str = Field(..., min_length=2)
    last_name: str = Field(..., min_length=2)
    phone: str = Field(..., pattern=r'^\(\d{3}\)\s\d{3}-\d{4}$')
    email: EmailStr
    address: str
    city: str
    province: str = Field(..., max_length=2)
    postal_code: str = Field(..., pattern=r'^[A-Z]\d[A-Z]\s\d[A-Z]\d$')
    rental_date: datetime = Field(default_factory=datetime.now)
    unit_type: str
    monthly_rate: float
    deposit_paid: float = 0.0