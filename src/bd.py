import mysql.connector as mys


def criaConexao(host, port, user, password, database):
    return mys.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
    )


def criaCursor(conexao):
    return conexao.cursor()







def consulta():
    vendas=[]
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)

    cursor.execute('select * from Produtos')
    result=cursor.fetchall()

    for r in result:
        vendas.append({
            'id':r[0],
            'item':r[1],
            'preco_uni':r[2],
            'quantidade':r[3]
        })
    
    
    
    return vendas

