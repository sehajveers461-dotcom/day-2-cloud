from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from schemas import TaskSchema
from model import Task

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to cloud task manager"}


@app.post("/create_task")
def create_task(task: TaskSchema, db: Session = Depends(get_db)):

    # Create Task object
    new_task = Task(
        task_title=task.task_title,
        description=task.description,
        assigned_to=task.assigned_to,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date,
        created_by=task.created_by
    )

    # Save to database
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks