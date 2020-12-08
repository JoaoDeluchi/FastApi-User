from pydantic import BaseModel


class CreateModel(BaseModel):
    first_name: str
    last_name: str
    password: str
    is_admin: bool

class ResponseModel(CreateModel):
    id: str
