from typing import List, Optional
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoStatus

class TodoService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo_create: TodoCreate) -> Todo:
        db_todo = Todo(
            title=todo_create.title,
            description=todo_create.description,
            status=todo_create.status
        )
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def get_all(self, status: Optional[TodoStatus] = None) -> List[Todo]:
        query = self.db.query(Todo)
        if status:
            query = query.filter(Todo.status == status)
        return query.all()
    
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self.db.query(Todo).filter(Todo.id == todo_id).first()
    
    def update(self, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
        db_todo = self.get_by_id(todo_id)
        if not db_todo:
            return None

        update_data = todo_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_todo, field, value)

        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def delete(self, todo_id: int) -> bool:
        db_todo = self.get_by_id(todo_id)
        if not db_todo:
            return False
        self.db.delete(db_todo)
        self.db.commit()
        return True