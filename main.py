## Atividade incompleta

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from repositories import produto_repo

app = FastAPI()
templates = Jinja2Templates(directory="templates")
PASTA_ESTATICA = "\static"

produto_repo.criar_tabela()
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
    if produto_repo.inserir_produto(nome, categoria, estoque, preco, descricao):
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        return RedirectResponse("/cadastro", 303)

  
@app.get("/cadastro_recebido")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})  


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)



