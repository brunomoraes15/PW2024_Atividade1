SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS produto (
    nome VARCHAR(40),
    descricao TEXT,
    estoque INT,
    preco FLOAT,
    categoria VARCHAR(20),
    id SERIAL PRIMARY KEY
);
"""

SQL_INSERIR = """
INSERT INTO produto (nome, descricao, estoque, preco, categoria)
VALUES (%s, %s, %s, %s, %s)
"""

SQL_EXCLUIR = """
DELETE FROM produto
WHERE id = %s;
"""

SQL_OBTER_TODOS = """
SELECT * FROM produto
"""
