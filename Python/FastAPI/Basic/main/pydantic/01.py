from pydantic import BaseModel


class PackBook(BaseModel):
    id: int
    Name: str
    Publishers: str
    Isbn: str
