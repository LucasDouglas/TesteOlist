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
    cursor.execute("UPDATE PRODUTOS SET NOME = ? , DESCRICAO = ? , VALOR = ? , FK_CATEGORIAS = ? WHERE IDPRODUTO = ? ", (var1, var2 ,var3 ,var4, var5))
    cursor.commit()

def Delete(var1):
    cursor = connection_sql()
    cursor.execute("DELETE FROM PRODUTOS WHERE IDPRODUTO = ?", (var1))
    cursor.commit()

def ReadName(var1):
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS WHERE NOME = ?;",(var1)) 
    lines = cursor.fetchall()
    for line in lines:
        print(line)

def ReadDescription(var1):
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS WHERE DESCRICAO = ?;",(var1)) 
    lines = cursor.fetchall()
    for line in lines:
        print(line)

def ReadValue(var1):
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS WHERE VALOR = ?;",(var1)) 
    lines = cursor.fetchall()
    for line in lines:
        print(line)
       
def ReadCategory(var1):
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS WHERE FK_CATEGORIAS = ?;",(var1)) 
    lines = cursor.fetchall()
    for line in lines:
        print(line)