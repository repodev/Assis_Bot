import sqlite3
con = sqlite3.connect('fotos.db')
cur = con.cursor()
cur.execute("SELECT * FROM imagens")

for linha in cur.fetchall():
    print linha
con.close()
