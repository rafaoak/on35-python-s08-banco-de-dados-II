import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

id = 2

# Atualizar um registro que ja existe
cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?", (41.99,id))

sql_query = (f'''
    SELECT titulo, genero, preco
    FROM filmes
    WHERE id = {id} 
''')

cursor.execute(sql_query)
resultado = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select
print(f'O preço do filme com id {id} foi atualizado com sucesso: ')
print(resultado)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()