from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.bd import consulta

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





@app.get('/')
def home():
    vendas=consulta()
    return {"qtd_vendas":len(vendas), "info_vendas":vendas}


@app.get('/vendas/{id_venda}')
def get_venda(id_venda:int):
    vendas=consulta()
    if (len(vendas)-1) >= id_venda and id_venda>-1:
        return vendas[id_venda]
    else:
        return {'erro':f'id da venda é inexistente.tente números entre 0 e {len(vendas)-1}'}


