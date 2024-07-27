import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

id = 2

sql_query = (f'''
    SELECT titulo, genero, preco
    FROM filmes
    WHERE id = {id} 
''')

cursor.execute(sql_query)
resultado = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

#Remover um registro da tabela
cursor.execute("DELETE FROM filmes WHERE id = ?", (id,)) #dessa forma, precisa colocar a virgula mesmo sem um outro parametro

print(f'O filme com o id {id} foi deletado com sucesso: {resultado}')

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()