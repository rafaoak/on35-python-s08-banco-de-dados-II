import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Criar a tabela de filmes
create_table_movies = ('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INT(4),
        genero TEXT,
        preco REAL
    )
''')

cursor.execute(create_table_movies)

# Salva as alterações no banco de dados
conn.commit()

print('Banco de dados da videoteca criado com sucesso!')

# Fecha a conexão
cursor.close()
conn.close()