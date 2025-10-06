from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.todo_service import TodoService


def get_todo_service(db: Session = Depends(get_db)):
    return TodoService(db)