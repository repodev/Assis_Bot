import sqlite3

conectar = sqlite3.connect('fotos.db')
c = conectar.cursor()

def criar_db():
    c.execute("""
    CREATE TABLE imagens (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        n_imagem TEXT NOT NULL,
        date INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        n_usuario TEXT NOT NULL,
        n_original TEXT NOT NULL
        )
    
    """
    )

try:
   criar_db()
except:
   print 'Erro ao criar!'
else:
   print 'Criado com sucesso!'
c.close()


