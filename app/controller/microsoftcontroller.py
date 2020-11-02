import pyodbc

def connection_sql():
       server = "DESKTOP-2DLJ3PV\SQLEXPRESS"
       database = "OLIST"
       string_connection = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
       connection = pyodbc.connect(string_connection)
       return connection.cursor()

if __name__ == "__main__":
    connection_sql()