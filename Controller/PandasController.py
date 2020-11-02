import sys
import pandas as pd
from ..Controller.MicrosoftController import connection_sql



def panda_connect():
  df = pd.read_csv("C:\Teste Olist\TesteOlist/Categorias.csv" , encoding= "ANSI" )
  cursor = connection_sql()
  for x in df.nome:
    cursor.execute("INSERT INTO CATEGORIAS (NOME) values(?)", x)
  return x

  
if __name__ == "__main__":
  panda_connect()
