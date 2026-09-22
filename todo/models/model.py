from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, ConfigDict
from pydantic import ValidationError
from typing import Annotated, Literal, List
from annotated_types import Gt, Ge, Le
from pydantic import StringConstraints

# todo 1 개
class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool
    important: bool

class Todo(BaseModel):
    # todos: list[TodoItem]
    todos: List[TodoItem]

    # Swagger/OpenAPI 문서에 보여줄 환경설정
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "todos":[
                    {
                        "id": 0,
                        "title": "sample title",
                        "completed": True,
                        "important": False
                    },
                ]
            }
        }
    )