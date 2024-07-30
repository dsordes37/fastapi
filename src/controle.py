from src.modelo import *

def getVendas():
    vendas=[]
    dados=listar()
    for item in dados:
        vendas.append({
            'id':item[0],
            'nome':item[1],
            'preco_uni':item[2],
            'quantidade':item[3]
        })
    
    return vendas


def getVendaById(id):
    dados=pesquisar(id)

    if dados != 'inválido':
        venda={
            'id':dados[0],
            'nome':dados[1],
            'preco_uni':dados[2],
            'quantidade':dados[3]
        }

        return venda
    else:
        return {'erro':f'id de venda é inexistente.'}

def insertVenda(nome, preco_unitario, quantidade):
    inserir(nome, preco_unitario, quantidade)

def updateVendaById(id, coluna, valor):
    editar(coluna, valor, id)

def deleteById(id):
    deletar(id)