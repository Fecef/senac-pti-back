from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)
    compras = relationship(
        "Compra", back_populates="cliente", order_by="Compra.total_comprado.desc()"
    )


class Compra(Base):
    __tablename__ = "compras"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    produto = Column(String)
    total_comprado = Column(Integer, default=1)
    cliente = relationship("Cliente", back_populates="compras")
    historico = relationship("Historico", back_populates="compra")


class Historico(Base):
    __tablename__ = "historico"
    id = Column(Integer, primary_key=True, index=True)
    compra_id = Column(Integer, ForeignKey("compras.id"))
    compra = relationship("Compra", back_populates="historico")
    comprado_em = Column(Date)
