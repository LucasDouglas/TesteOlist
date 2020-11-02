import pyodbc


def retornar_conexao_sql():
    server = "DESKTOP-2DLJ3PV\SQLEXPRESS"
    database = "OLIST"
    #username = "aula_mongodb"
    #password = "abc123"
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()
    

cursor = retornar_conexao_sql()

var1 = input("digite o produto :")
var2 = input("descrição do produto :")
var3 = int(input("valor do produto :"))
var4 = float(input("Categoria:"))

sql = ("INSERT INTO PRODUTOS (NOME, DESCRICAO, VALOR, FK_CATEGORIAS)VALUES (?, ?, ?, ?)" , (var1, var2 , var3 , var4 ))


cursor.execute("INSERT INTO PRODUTOS (NOME, DESCRICAO, VALOR, FK_CATEGORIAS)VALUES (?, ?, ?, ?)" , (var1, var2 ,var3 ,var4 ))

print(type(var3))
print(type(var4))

sql = "SELECT * FROM PRODUTOS;"
cursor.execute(sql)

#linha = cursor.fetchone()
#linhas = cursor.fetchone()
linhas = cursor.fetchall()

for linha in linhas:
    print(linha)

sql = "SELECT * FROM CATEGORIAS;"
cursor.execute(sql)

#linha = cursor.fetchone()
#linhas = cursor.fetchone()
linhas = cursor.fetchall()

for linha in linhas:
    print(linha)



var5 = input("digite 1 para alterar o nome do produto - digite 2 para alterar o nome do produto - digite 3 para alterar o nome do produto - digite 4 para alterar o nome do produto :")

if var5 == "1":
    var9 = "NOME"
    var6 = input("Novo nome do produto")

cursor.execute("UPDATE PRODUTOS SET NOME = 'XUMBETA' WHERE IDPRODUTO = 2")
