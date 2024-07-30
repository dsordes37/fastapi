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







def listar():
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)

    cursor.execute('select * from Produtos')
    dados=cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados




def pesquisar(id):
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)

    cursor.execute(f"SELECT * FROM Produtos WHERE id={id};")
    dados=cursor.fetchall()

    cursor.close()
    conexao.close()

    if dados==[]:
        return 'inválido'
    else:
        return dados[0]




def inserir(nome, preco_unitario, quantidade):
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)

    valores=[nome, preco_unitario, quantidade]

    cursor.execute("INSERT INTO Produtos(nome, preco_uni, quantidade) VALUES(%s, %s, %s);", valores)
    conexao.commit()

    conexao.close()
    cursor.close()




def editar(coluna, valor, id):
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)
    valores=[coluna, valor, id]

    cursor.execute(F"UPDATE Produtos SET {coluna}='{valor}' WHERE id={id}")
    conexao.commit()

    conexao.close()
    cursor.close()




def deletar(id):
    conexao=criaConexao("monorail.proxy.rlwy.net",'25969',"root","IDpNJKkbCupRBHxeslRyoYRGfoZTPKmB","railway",)
    cursor=criaCursor(conexao)

    cursor.execute(f"DELETE FROM Produtos WHERE id={id}")
    conexao.commit()

    conexao.close()
    cursor.close()
