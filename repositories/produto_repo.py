from typing import Optional
from models.produto_model import Produto
from utils import *
from sql import produto_sql

def criar_tabela():
    with obter_conexao as con:
        bd = con.cursor()
        bd.execute(produto_sql.SQL_CRIAR_TABELA)

def inserir_produto(produto: Produto) -> Optional[Produto]:
    bd = obter_conexao.cursor()
    bd.execute(produto_sql.SQL_INSERIR, (
        produto.nome,
        produto.categoria,
        produto.estoque,
        produto.preco,
        produto.descricao   

    ))

def obter_todos():
    bd = obter_conexao.cursor()
    bd.execute(produto_sql.SQL_OBTER_TODOS)