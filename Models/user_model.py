from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name : str
    email : EmailStr
    password : str

class UpdateUser(BaseModel):
    name : str | None = None
    email : EmailStr | None = None
    password : str | None = None