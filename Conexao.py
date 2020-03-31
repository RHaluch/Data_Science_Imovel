from mysql.connector import (connection)

def conectar ():
    conexao = connection.MySQLConnection(host='127.0.0.1', user='root', password='root', database='db')
    return conexao

def desconectar(conexao):
    conexao.close()

def executarQuery(query, conexao):
    cursor = conexao.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def executarInsert(query, conexao):
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
