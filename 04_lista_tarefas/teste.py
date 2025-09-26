import sqlite3

# dar nome pro banco de dados
conexão = sqlite3.connect('Banco de dados')
cursor = conexão.cursor()

# criar as tabelas
cursor.execute('''CREATE TABLE aluno
               (id INT PRIMARY KEY, nome TEXT, idade INT)'''
)





