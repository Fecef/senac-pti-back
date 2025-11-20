from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class HistoricoOut(BaseModel):
    comprado_em: date

    class Config:
        orm_mode = True


class CompraCreate(BaseModel):
    cliente_id: int
    produto: str


class CompraOut(BaseModel):
    id: int
    produto: str
    total_comprado: int
    historico: List[HistoricoOut] = []

    class Config:
        orm_mode = True


class ClienteCreate(BaseModel):
    cpf: str
    telefone: str


class ClienteUpdate(BaseModel):
    cpf: Optional[str] = None
    telefone: Optional[str] = None

    class Config:
        orm_mode = True


class ClienteOut(BaseModel):
    id: int
    cpf: str
    telefone: str
    compras: List[CompraOut] = []

    class Config:
        orm_mode = True


class Sugestao(BaseModel):
    produto: str
    motivo: str
