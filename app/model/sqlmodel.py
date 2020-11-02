from os import path
from controller.microsoftcontroller import connection_sql



def Create(var1, var2 ,var3 ,var4 ):
    cursor = connection_sql()
    cursor.execute("INSERT INTO PRODUTOS (NOME, DESCRICAO, VALOR, FK_CATEGORIAS)VALUES (?, ?, ?, ?)", (var1, var2 ,var3 ,var4 ))
    cursor.commit()


def ReadAll():
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS;")
    lines = cursor.fetchall()
    for line in lines:
        print(line)

def ReadAll2():
    cursor = connection_sql()
    cursor.execute("SELECT * FROM CATEGORIAS;")
    lines = cursor.fetchall()
    for line in lines:
        print(line)

def Alterate(var1, var2 ,var3 ,var4, var5):
    cursor = connection_sql()
    cursor.execute("UPDATE PRODUTOS SET NOME = ? , SET DESCRICAO = ?, SET VALOR = ?, SET FK_CATEGORIAS = ? WHERE IDPRODUTO = ?", (var1, var2 ,var3 ,var4, var5))
    cursor.commit()

def Delete(var1):
    cursor = connection_sql()
    cursor.execute("DELETE FROM PRODUTOS WHERE IDPRODUTO = ?", (var1))
    cursor.commit()


