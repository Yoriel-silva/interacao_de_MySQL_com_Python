import pyodbc

dados = (
    "Driver={driver};"
    "User=your_user;"
    "Password=your_pass;"
    "Server=your_server;"
    "DataBase=your_database;"
)

nome = str(input('Qual o seu nome? '))
usuario = str(input('Qual será seu nome de usuario? '))
senha = str(input('Qual será sua senha? '))

conexao = pyodbc.connect(dados)
print("yes")

cursor = conexao.cursor()

comando = f"""insert into dados values(
    default, '{nome}', '{usuario}', '{senha}');"""

cursor.execute(comando)
cursor.commit()