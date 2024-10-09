from typing import Optional
from models.produto_model import Produto
from utils import *
from sql.produto_sql import *



def criar_tabela():
        bd =  obter_conexao()
        bd = bd.cursor()
        bd.execute(SQL_CRIAR_TABELA)


def inserir_produto(produto: Produto) -> Optional[Produto]:
    bd =  obter_conexao()
    bd = bd.cursor()
    bd.execute(SQL_INSERIR, (
        produto.nome,
        produto.categoria,
        produto.estoque,
        produto.preco,
        produto.descricao   
    ))
    bd.close() 


def obter_todos():
    bd = obter_conexao.cursor()
    bd.execute(SQL_OBTER_TODOS)