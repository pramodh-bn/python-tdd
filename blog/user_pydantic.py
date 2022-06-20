from pydantic import BaseModel, EmailStr


class UserPydantic(BaseModel):
    email: EmailStr

user = UserPydantic(email='abc@abc.com')



