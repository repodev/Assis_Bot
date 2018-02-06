# encoding: utf-8
import hashlib
import time
from datetime import datetime
import os.path
from banco import *

def recebeComandoFotos(ms,msg):
    id_u = msg['from']['id']
    c.execute('SELECT date FROM imagens WHERE date=? and id_usuario=?', (ms[1:],id_u,)) #selecionando apenas as imagens com base no id do usuario
    d =  c.fetchone()
    if not d:
      return False
    else:
      return d[0]
    

def enviarFotosData(m,msg,bot,chat_id):
    id_u = msg['from']['id'] #capturando o id do usuario que pediu para listar
    c.execute('SELECT n_imagem FROM imagens WHERE date=? and id_usuario=?', (m[1:],id_u,)) #selecionando apenas as imagens com base no id do usuario
    cols =  c.fetchone() #executando uma consulta que retorna todos os registros - ALL
    foto = cols[0]
    bot.sendPhoto(chat_id,open(foto,'rb')) #abrindo somente leitura e enviando

def debugMenssagens(c,msg):
    nome = msg['from']['first_name']
    id_usuario = msg['from']['id']
    if c == 'text':
        texto = msg['text']
        print "Recebendo texto"
        print "ID:",id_usuario,nome,"Diz:",texto        
    elif c == 'photo':
        print nome,"Diz: Enviando fotos"

def baixarFotos(bot,msg,chat_id):
    #id imagem, para recuperar do servidor do telegram
    fotos = msg['photo'][-1]['file_id'] 
    #gera uma hash unica com base no id da imagem, para evitar duplicidade de nomes
    nome_imagem = hashlib.md5(fotos).hexdigest()
    #data que mensagem foi enviada
    data = msg['date']
    nome = msg['from']['first_name']
    id_usuario = msg['from']['id']
    #gerando nome da imagem e concatenando com id do usuario
    imagem = str(msg["from"]['id'])+'_'+nome_imagem[20:32]+".jpg"
    if (os.path.exists(imagem)):
      bot.sendMessage(chat_id,"Acho que já salvei essa foto, desculpe, minha memória é fraca!")
    else:
      bot.sendMessage(chat_id,"Armazenada com sucesso :)")
      inserir_imagens(imagem,data,id_usuario,nome,fotos)
      bot.download_file(fotos,imagem)
      


def geraComandosFotos(bot,msg,chat_id):
    id_u = msg['from']['id'] #capturando o id do usuario que pediu para listar
    c.execute('SELECT n_imagem,date FROM imagens WHERE id_usuario=?', (id_u,)) #selecionando apenas as imagens com base no id do usuario
    rows =  c.fetchall() #executando uma consulta que retorna todos os registros - ALL
    if not rows: #verificando se esta vazio
      bot.sendMessage(chat_id,"Nenhuma foto localizada, take a picture")
    else:
      bot.sendMessage(chat_id,"Gerando comandos, aguarde...")
      time.sleep(2)
      total = str(len(rows))
      if total > "1":
        bot.sendMessage(chat_id, total+" Fotos foram localizadas...")
      else:
        bot.sendMessage(chat_id, total+" Foto foi localizada...")
      
      #for para resultados em data timestamp
      for date in rows:
          #convertendo de timestamp para datetime
          con_data = datetime.fromtimestamp(date[1])
          #formatando a data
          data_mensagem = str(con_data.strftime("%d-%m-%Y às %H:%M %p"))
          #gerando estrutura do comando
          comando = "/"+str(date[1])
          bot.sendMessage(chat_id, comando+" - "+data_mensagem)

def horaOnibus(bot,msg,chat_id):
    id_u = msg['from']['id']
    bot.sendMessage(chat_id,"Não se atrase, corra como o vento e não perderá o onibus")
    bot.sendPhoto(chat_id,open("box/onb.jpg", 'rb'))
    bot.sendMessage(chat_id,"run forrest run")

def professor(bot,msg,chat_id):
    id_u = msg['from']['id']
    bot.sendMessage(chat_id,"Cara, você é muito preguiçoso, deixe eu andar com você no recreio?")
    bot.sendPhoto(chat_id,open("box/prof.jpg", 'rb'))

