from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Cliente, Compra
from schemas import ClienteCreate, ClienteOut, CompraCreate, Sugestao
from utils import enviar_notificacao

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes/", response_model=ClienteOut)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = Cliente(cpf=cliente.cpf, telefone=cliente.telefone)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.post("/compras/")
def registrar_compra(compra: CompraCreate, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == compra.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    nova_compra = Compra(cliente_id=compra.cliente_id, produto=compra.produto, valor=compra.valor)
    db.add(nova_compra)
    db.commit()
    db.refresh(nova_compra)
    enviar_notificacao(cliente, f"Obrigado pela compra de {compra.produto}!")
    return {"mensagem": "Compra registrada com sucesso"}

@app.get("/sugestoes/{cliente_id}", response_model=List[Sugestao])
def gerar_sugestoes(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    produtos = [compra.produto for compra in cliente.compras]
    sugestoes = []
    if "biscoito" in produtos:
        sugestoes.append(Sugestao(produto="biscoito recheado", motivo="Você costuma comprar biscoitos"))
    if "sabão" in produtos:
        sugestoes.append(Sugestao(produto="amaciante", motivo="Complementa sua compra de sabão"))
    return sugestoes
