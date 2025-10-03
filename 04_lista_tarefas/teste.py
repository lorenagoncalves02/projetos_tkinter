import sqlite3

# dar nome pro banco de dados
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# criar as tabelas
cursor.execute('''CREATE TABLE aluno
               (id INT PRIMARY KEY, nome TEXT, idade INT)'''
)







