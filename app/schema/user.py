from pydantic import BaseModel

from app.schema.post import PostRead  #menggunakan pydantic untuk membedakan mana model, mana schema


class UserCreate(BaseModel):
    full_name:str
    email: str
    password: str

class UserRead(BaseModel):
    id: str
    full_name: str
    email: str
    posts: list["PostRead"] = []
