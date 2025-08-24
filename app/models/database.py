from sqlmodel import Field, Relationship, SQLModel, String

from app.utils.generate_id import generate_id


class User(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True, sa_type=String)
    full_name: str = Field(default="")
    email: str = Field(unique=True)
    password: str | None

    posts: list["Post"] = Relationship(back_populates="user")

class Post(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    title: str = Field(default="")
    content: str = Field(default="")

    user_id: str = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="posts")
