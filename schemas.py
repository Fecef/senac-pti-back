from pydantic import BaseModel

class ClienteCreate(BaseModel):
    cpf: str
    telefone: str

class ClienteOut(BaseModel):
    id: int
    cpf: str
    telefone: str
    class Config:
        orm_mode = True

class CompraCreate(BaseModel):
    cliente_id: int
    produto: str
    valor: float

class Sugestao(BaseModel):
    produto: str
    motivo: str
