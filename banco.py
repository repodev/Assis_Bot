import sqlite3, time
conectar = sqlite3.connect('fotos.db')
c = conectar.cursor()

def inserir_imagens(n, d, id_u,n_u,n_o):
    c.execute("""
    INSERT INTO imagens(n_imagem,date,id_usuario,n_usuario,n_original) VALUES(?,?,?,?,?)
    """,(n, d, id_u,n_u,n_o))
    conectar.commit()
    print "dados inseridos"

