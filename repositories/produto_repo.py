from typing import Optional
from models.produto_model import Produto
from utils import *
from sql.produto_sql import *



def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)


def inserir_produto(produto: Produto) -> Optional[Produto]:
    with obter_conexao() as conexao:
        bd = conexao.cursor()
        bd.execute(SQL_INSERIR, (
            produto.nome,
            produto.categoria,
            produto.estoque,
            produto.preco,
            produto.descricao   
    ))
    if bd.rowcount > 0:
            produto.id = bd.lastrowid
            return produto
    else:
            return None


def obter_todos():
    bd = obter_conexao.cursor()
    bd.execute(SQL_OBTER_TODOS)