from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from repositories.produto_repo import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")
#PASTA_ESTATICA = "\static"

criar_tabela()
print("tabela criada")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request,
    nome: str = Form(...), 
    categoria: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...), 
    preco: float = Form(...)):

    produto = Produto(
        nome=nome,
        categoria=categoria,
        descricao=descricao,
        estoque=estoque,
        preco=preco
    )
    produto_inserido = inserir_produto(produto)
    
    if produto_inserido:
        print('passou')
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        print('não passou')
        return RedirectResponse("/cadastro", 303)

  
@app.get("/cadastro_recebido")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})  


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)



