from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional

# Pydantic Model
class StorageUnit(BaseModel):
    unit: str
    status: str
    unit_type: str = Field(alias="Unit Type")
    customer: Optional[str] = None
    phone: Optional[str] = None
    cell_phone: Optional[str] = Field(None, alias="Cell Phone")
    email: Optional[str] = None
    balance: float = 0.0