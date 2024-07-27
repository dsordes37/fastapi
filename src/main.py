from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.controle import *


class Venda(BaseModel):
    nome:str
    valor_uni:float
    quantidade:int    


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500/",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')




@app.get('/')
async def home():
    vendas=getVendas()
    return {"qtd_vendas":len(vendas), "info_vendas":vendas}


@app.get('/pesquisa')
async def get_venda(id:int):
    return getVendaById(id)


@app.post('/insert')
async def insert_venda(venda:Venda):
    insertVenda(venda.nome, venda.valor_uni, venda.quantidade)
    return {
        'mensagem':'dados inseridos com sucesso',
        'dados':venda
    }


#MÉTODOS HTTP: GET POST PUT DELETE
