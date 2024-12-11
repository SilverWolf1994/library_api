from pydantic import BaseModel
from datetime import datetime

class BaseBook(BaseModel):
    isbn: str
    title: str
    author: str
    year: str
    published: bool
    created: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    class ConfigDict:
        from_attributes = True

class CreateBook(BaseBook):
    class ConfigDict:
        from_attributes = True
