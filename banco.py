import sqlite3
import os.path

conexao = cursor = None


def abre_conexao():
    global cursor, conexao
    conexao = sqlite3.connect('fotos.db', check_same_thread=False)
    cursor = conexao.cursor()


def fecha_conexao():
    global conexao
    conexao.close()


def verifica_db():
    if not os.path.exists("fotos.db"):
        try:
            abre_conexao()
            criar_db()
            print 'Criado com sucesso!'
        except Exception as e:
            print 'Erro ao criar!'
            print e
    else:
        abre_conexao()


def criar_db():
    global cursor
    cursor.execute("""
    CREATE TABLE imagens (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        n_imagem TEXT NOT NULL,
        date INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        n_usuario TEXT NOT NULL,
        n_original TEXT NOT NULL
        )
    
    """)


def inserir_imagens(n, d, id_u, n_u, n_o):
    global cursor, conexao
    cursor.execute("""
    INSERT INTO imagens(n_imagem,date,id_usuario,n_usuario,n_original) VALUES(?,?,?,?,?)
    """, (n, d, id_u, n_u, n_o))
    conexao.commit()
    print "dados inseridos"


def select_images_date(date, user):
    global cursor
    cursor.execute('SELECT date FROM imagens WHERE date=? and id_usuario=?', (date, user,))
    d = cursor.fetchone()
    if not d:
        return False
    else:
        return d[0]


def select_images_name_date(user):
    global cursor
    cursor.execute('SELECT n_imagem, date FROM imagens WHERE id_usuario=?', (user,))
    return cursor.fetchall()

