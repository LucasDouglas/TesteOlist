from os import path
from ..Controller.MicrosoftController import connection_sql



def Create(var1, var2 ,var3 ,var4 ):
    cursor = connection_sql()
    cursor.execute("INSERT INTO PRODUTOS (NOME, DESCRICAO, VALOR, FK_CATEGORIAS)VALUES (?, ?, ?, ?)", (var1, var2 ,var3 ,var4 ))


def ReadAll():
    cursor = connection_sql()
    cursor.execute("SELECT * FROM PRODUTOS;")
    lines = cursor.fetchall()
    for line in lines:
        print(line)

def Alterate(var1, var2 ,var3 ,var4, var5):
    cursor = connection_sql()
    cursor.execute("UPDATE PRODUTOS SET NOME = ? , SET DESCRICAO = ?, SET VALOR = ?, SET FK_CATEGORIAS = ? WHERE IDPRODUTO = ?", (var1, var2 ,var3 ,var4, var5))

def Delete(var1):
    cursor = connection_sql()
    cursor.execute("DELETE FROM PRODUTOS WHERE IDPRODUTO = ?", (var1))

if __name__ == "__main__":
    var1 = 'DILDO DO KID'
    var2 = 'PRETO COM VEIAS TORTÃO PRA DIREITA'
    var3 = 120.00
    var4 = 1

    Create(var1, var2, var3, var4)

    ReadAll()
