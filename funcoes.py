# encoding: utf-8
import hashlib
import time
from datetime import datetime
import os.path
from banco import *


def recebeComandoFotos(text, msg):
    id_u = msg['from']['id']
    for i in select_images_name_date(id_u):
        if os.path.basename(i[0])[:12] == text[1:]:
            return True
    return False


def enviarFotosData(m, msg, bot, chat_id):
    id_u = msg['from']['id']  # capturando o id do usuario que pediu para listar
    for c in select_images_name_date(id_u):
        if os.path.basename(c[0])[:12] == m[1:]:
            foto = c[0]
            bot.sendPhoto(chat_id, open(foto, 'rb'))  # abrindo somente leitura e enviando


def debugMenssagens(c, msg):
    nome = msg['from']['first_name']
    id_usuario = msg['from']['id']
    if c == 'text':
        texto = msg['text']
        print "Recebendo texto"
        print "ID:", id_usuario, nome, "Diz:", texto
    elif c == 'photo':
        print nome, "Diz: Enviando fotos"


def baixarFotos(bot, msg, chat_id, FLAG=None):
    fotos = msg['photo'][-1]['file_id']
    if FLAG is not None:
        if FLAG == 1:
            nome_imagem = "box/onb.jpg"
        elif FLAG == 2:
            nome_imagem = "box/prof.jpg"
        bot.download_file(fotos, os.path.join(os.path.abspath("./"), nome_imagem))
        bot.sendMessage(chat_id, "Armazenada com sucesso :)")
    else:
        nome_imagem = hashlib.md5(str(time.time())).hexdigest()
        data = msg['date']
        nome = msg['from']['first_name']
        id_usuario = msg['from']['id']
        imagem = os.path.join(os.path.abspath("./box"), nome_imagem[20:32]+"_"+str(msg["from"]['id'])+".jpg")
        if os.path.exists(imagem):
            bot.sendMessage(chat_id, "Acho que já salvei essa foto, desculpe, minha memória é fraca!")
        else:
            bot.sendMessage(chat_id, "Armazenada com sucesso :)")
            inserir_imagens(imagem, data, id_usuario, nome, fotos)
            bot.download_file(fotos, imagem)
      

def geraComandosFotos(bot, msg, chat_id):
    id_u = msg['from']['id']
    rows = select_images_name_date(id_u)
    if not rows:
        bot.sendMessage(chat_id, "Nenhuma foto localizada, take a picture")
    else:
        bot.sendMessage(chat_id, "Gerando comandos, aguarde...")
        time.sleep(2)
        total = str(len(rows))
        if total > "1":
            bot.sendMessage(chat_id, total + " Fotos foram localizadas...")
        else:
            bot.sendMessage(chat_id, total + " Foto foi localizada...")
    for date in rows:
        con_data = datetime.fromtimestamp(date[1])
        data_mensagem = str(con_data.strftime("%d-%m-%Y às %H:%M %p"))
        comando = "/"+str(os.path.basename(date[0])[:12])
        bot.sendMessage(chat_id, comando+" - "+data_mensagem)


def horaOnibus(bot, msg, chat_id):
    if os.path.exists("box/onb.jpg"):
        bot.sendMessage(chat_id,"Não se atrase, corra como o vento e não perderá o onibus")
        bot.sendPhoto(chat_id,open("box/onb.jpg", 'rb'))
        bot.sendMessage(chat_id,"run forrest run")
    else:
        bot.sendMessage(chat_id, "Não encontrei os horarios do seu onibus, se quiser me atualizar, me envie /uponb!")


def professor(bot, msg, chat_id):
    if os.path.exists("box/prof.jpg"):
        bot.sendMessage(chat_id,"Cara, você é muito preguiçoso, deixe eu andar com você no recreio?")
        bot.sendPhoto(chat_id,open("box/prof.jpg", 'rb'))
    else:
        bot.sendMessage(chat_id, "Não encontrei os contatos dos seus professores, se quiser me atualizar, me envie /upprof!")


def verifica_pastas():
    caminho = os.path.join(os.path.abspath("./box"))
    if not os.path.exists(caminho):
        os.mkdir(caminho)

