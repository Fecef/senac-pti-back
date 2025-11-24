import random
from datetime import date, timedelta

from sqlalchemy.orm import Session

from database import SessionLocal
from models import Cliente, Compra, Historico

PRODUTOS = [
    "Arroz Tio João",
    "Feijão Carioca",
    "Macarrão Renata",
    "Café Pilão",
    "Açúcar União",
    "Óleo Soya",
    "Detergente Ypê",
    "Sabão em Pó OMO",
    "Papel Higiênico Neve",
    "Leite Italac",
    "Biscoito Bono",
]


def gerar_data_aleatoria(qtd_dias=120):
    """Retorna uma data entre hoje e X dias atrás."""
    return date.today() - timedelta(days=random.randint(0, qtd_dias))


def seed():
    db: Session = SessionLocal()

    db.query(Historico).delete()
    db.query(Compra).delete()
    db.query(Cliente).delete()
    db.commit()

    for i in range(1, 11):
        cliente = Cliente(
            cpf=f"000000000{i:02}",
            telefone=f"119999900{i:02}",
        )
        db.add(cliente)
        db.commit()
        db.refresh(cliente)

        for _ in range(random.randint(2, 4)):
            produto_escolhido = random.choice(PRODUTOS)

            compra = Compra(
                cliente_id=cliente.id, produto=produto_escolhido, total_comprado=0
            )
            db.add(compra)
            db.commit()
            db.refresh(compra)

            historicos_qtd = random.randint(1, 6)

            for _ in range(historicos_qtd):
                hist = Historico(
                    compra_id=compra.id, comprado_em=gerar_data_aleatoria()
                )
                db.add(hist)

            compra.total_comprado = historicos_qtd

            db.commit()

    print("✔️ Seed executado com sucesso! 10 clientes criados.")


if __name__ == "__main__":
    seed()
