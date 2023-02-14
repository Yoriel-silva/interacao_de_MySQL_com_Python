import pyodbc

dados = (
    "Driver={****};"
    "User=****;"
    "Password=****;"
    "Server=****;"
    "DataBase=****;"
)

conexao = pyodbc.connect(dados)
print("yes")