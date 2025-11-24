from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, Cliente, Compra, Historico
from schemas import (
    ClienteCreate,
    ClienteDetailOut,
    ClienteOut,
    ClienteUpdate,
    CompraCreate,
)

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8080",
    "*"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes/", response_model=ClienteOut)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    cliente = Cliente(cpf=cliente.cpf, telefone=cliente.telefone)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@app.patch("/clientes/{cpf}/", response_model=ClienteOut)
def atualizar_cliente(cpf: str, dados: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente nao encontrado")

    if dados.cpf is not None:
        cliente.cpf = dados.cpf
    
    if dados.telefone is not None:
        cliente.telefone = dados.telefone

    db.commit()
    db.refresh(cliente)
    return cliente

@app.delete("/clientes/{cpf}/")
def deletar_cliente(cpf: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente nao encontrado")

    db.delete(cliente)
    db.commit()

    return cliente

@app.get("/clientes/{cpf}/", response_model=ClienteDetailOut)
def detalhe_cliente(cpf: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente nao encontrado")
    
    return cliente

@app.get("/clientes/", response_model=List[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    resposta = []

    for cliente in clientes:
        datas = [
            hist.comprado_em
            for compra in cliente.compras
            for hist in compra.historico
        ]

        ultima_data = max(datas) if datas else None

        resposta.append(
            ClienteOut(
                id=cliente.id,
                cpf=cliente.cpf,
                telefone=cliente.telefone,
                ultima_compra=ultima_data,
            )
        )

    return resposta

@app.post("/compras/")
def registrar_compra(dados_compra: CompraCreate, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == dados_compra.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    nome_base_produto = dados_compra.produto.split()[0]
    compra = db.query(Compra).filter(Compra.cliente_id == dados_compra.cliente_id, Compra.produto.ilike(f"%{nome_base_produto}%")).first()
    compra = compra or Compra(cliente_id=dados_compra.cliente_id, produto=nome_base_produto)
    compra.total_comprado = (compra.total_comprado or 0)+1
    Historico(comprado_em=datetime.now().date(), compra=compra)
        
    db.add(compra)
    db.commit()
    db.refresh(compra)
    return compra

@app.get("/clientes/{cpf}/compras/ranking", response_model=ClienteOut)
def ranking_compras_por_cliente(cpf: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente nao encontrado")
    
    return cliente

@app.get("/sugestoes/{cpf}")
def enviar_mensagem(cpf: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    produtos = [compra.produto for compra in cliente.compras]
    mensagem = f"{produtos[0]} acaba de entrar em promoção! Venha conferir!"

    return mensagem
