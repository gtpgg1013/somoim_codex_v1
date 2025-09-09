from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, SessionLocal, engine

app = FastAPI(title="Somoim API")

# Create database tables
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok"}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        email=user.email,
        nickname=user.nickname,
        password_hash=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/groups", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    db_group = models.Group(
        name=group.name,
        description=group.description,
        owner_id=group.owner_id,
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


@app.post("/groups/{group_id}/members")
def add_group_member(
    group_id: int, membership: schemas.MembershipCreate, db: Session = Depends(get_db)
):
    member = models.GroupMember(
        user_id=membership.user_id, group_id=group_id, role=membership.role
    )
    db.add(member)
    db.commit()
    return {"status": "member added"}


@app.post("/groups/{group_id}/posts", response_model=schemas.Post)
def create_post(group_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(
        group_id=group_id,
        author_id=post.author_id,
        title=post.title,
        content=post.content,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.post("/posts/{post_id}/comments", response_model=schemas.Comment)
def create_comment(
    post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)
):
    db_comment = models.Comment(
        post_id=post_id, author_id=comment.author_id, content=comment.content
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@app.post("/groups/{group_id}/events", response_model=schemas.Event)
def create_event(
    group_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)
):
    db_event = models.Event(
        group_id=group_id,
        title=event.title,
        description=event.description,
        location=event.location,
        start_time=event.start_time,
        end_time=event.end_time,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@app.post("/events/{event_id}/participants")
def add_event_participant(
    event_id: int,
    participant: schemas.EventParticipantCreate,
    db: Session = Depends(get_db),
):
    db_part = models.EventParticipant(
        event_id=event_id, user_id=participant.user_id, status=participant.status
    )
    db.add(db_part)
    db.commit()
    return {"status": "participant added"}


@app.post("/users/{user_id}/notifications", response_model=schemas.Notification)
def create_notification(
    user_id: int, notification: schemas.NotificationCreate, db: Session = Depends(get_db)
):
    db_notif = models.Notification(
        user_id=user_id, type=notification.type, data=notification.data
    )
    db.add(db_notif)
    db.commit()
    db.refresh(db_notif)
    return db_notif
