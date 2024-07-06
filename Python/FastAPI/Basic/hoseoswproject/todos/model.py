from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(id=1, item=item)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Exameple Schema!"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
