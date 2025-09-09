from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    nickname: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str
    description: str | None = None


class GroupCreate(GroupBase):
    owner_id: int


class Group(GroupBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class MembershipCreate(BaseModel):
    user_id: int
    role: str = "member"


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    author_id: int


class Post(PostBase):
    id: int
    group_id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    author_id: int
    content: str


class Comment(BaseModel):
    id: int
    post_id: int
    author_id: int
    content: str
    created_at: datetime

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    title: str
    description: str | None = None
    location: str | None = None
    start_time: datetime
    end_time: datetime


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    group_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class EventParticipantCreate(BaseModel):
    user_id: int
    status: str = "going"


class EventParticipant(BaseModel):
    event_id: int
    user_id: int
    status: str
    joined_at: datetime

    class Config:
        orm_mode = True


class NotificationCreate(BaseModel):
    type: str
    data: dict | None = None


class Notification(BaseModel):
    id: int
    user_id: int
    type: str
    data: dict | None = None
    is_read: bool
    created_at: datetime

    class Config:
        orm_mode = True

