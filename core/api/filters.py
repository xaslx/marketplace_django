from pydantic import BaseModel
from ninja import Schema



class PaginationIn(Schema):
    limit: int = 20
    offset: int = 0




class PaginationOut(Schema):
    offset: int
    limit: int
    total: int

