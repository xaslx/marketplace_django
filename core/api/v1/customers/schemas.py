from ninja import Schema


class AuthInSchema(Schema):
    phone: str


class AuthOutSchema(Schema):
    message: str


class TokenInSchema(Schema):
    code: str
    phone: str


class TokenOutSchema(Schema):
    token: str