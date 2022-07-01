import datetime

from flask import Flask, request
from flask_pydantic import validate
from pydantic import BaseModel

app = Flask(__name__)

class CreateTodo(BaseModel):
    title: str
    done: bool
    deadline: datetime.date

class Todo(BaseModel):
    title: str
    done: bool
    deadline: datetime.date
    created_at: datetime.datetime

@app.route("/todos/", methods=["POST"])
@validate(body=CreateTodo)
def todos():
    todo = Todo(
        title=request.body_params.title,
        done=request.body_params.done,
        deadline=request.body_params.deadline,
        created_at=datetime.datetime.now()
    )
    return todo, 201

if __name__ == "__main__":
    app.run()