from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import mysql.connector as mys

conexao = mys.connect(
    host="monorail.proxy.rlwy.net",
    port='48006',
    user="root",
    password="cXYGNalOPUlWwDaGqVvOLaLxQvZTbvSh",
    database="railway",
)

cursor=conexao.cursor()


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

vendas=[]

cursor.execute('select * from produtos')
result=cursor.fetchall()

for r in result:
    vendas.append({
        'item':r[1],
        'preco_uni':r[2],
        'quantidade':r[3]
    })



@app.get('/')
def home():
    return {"qtd_vendas":len(vendas), "info_vendas":vendas}


@app.get('/vendas/{id_venda}')
def get_venda(id_venda:int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'erro':f'id da venda é inexistente.tente números entre 1 e {len(vendas)}'}
