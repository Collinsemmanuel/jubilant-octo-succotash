from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse, TodoStatus
from app.services.todo_service import TodoService
from app.api.deps import get_todo_service

router = APIRouter()

@router.post("/", response_model=TodoResponse, status_code=201)
async def create_todo(
    todo: TodoCreate, 
    todo_service: TodoService = Depends(get_todo_service)
):
    """
    Create a new todo
    """
    new_todo = todo_service.create(todo)
    return TodoResponse.model_validate(new_todo)

@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    status: Optional[TodoStatus] = None,
    todo_service: TodoService = Depends(get_todo_service)
):
    """
    Get all todos
    """
    todos = todo_service.get_all(status)
    return [TodoResponse.model_validate(todo) for todo in todos]

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: int,
    todo_service: TodoService = Depends(get_todo_service)
):
    """
    Get a todo by id
    """
    todo = todo_service.get_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponse.model_validate(todo)

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    todo_service: TodoService = Depends(get_todo_service)
):
    """
    Update a todo by id
    """
    updated_todo = todo_service.update(todo_id, todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponse.model_validate(updated_todo)

@router.delete("/{todo_id}", status_code=204)
async def delete_todo(
    todo_id: int,
    todo_service: TodoService = Depends(get_todo_service)
):
    """
    Delete a todo by id
    """
    success = todo_service.delete(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None