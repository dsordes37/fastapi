import mysql.connector as mys


conexao = mys.connect(
    host="monorail.proxy.rlwy.net",
    port='25969',
    user="root",
    password="IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB",
    database="railway",
)


cursor=conexao.cursor()







def consulta():
    vendas=[]
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

