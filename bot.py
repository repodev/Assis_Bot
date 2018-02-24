# -*- encoding: utf-8
import telepot
from telepot.loop import MessageLoop
from funcoes import *
from banco import verifica_db, fecha_conexao
from exceptions import KeyboardInterrupt

TOKEN = ""
bot = telepot.Bot(TOKEN)
FLAG = None


def corpo(msg):
    global FLAG
    content_type, chat_type, chat_id = telepot.glance(msg)
    usu = []
    ids = msg['from']['id']
    debugMenssagens(content_type, msg)
    if (content_type == 'text') and (ids in usu):
        texto = msg['text'].lower()
        if texto == '/start':
            bot.sendMessage(chat_id, """
Bem vindo calouro, me chamo AssiS, e os meus comandos são os seguintes:

*/listar* = Fotos que firam salvas.
*/onb* = Horário do onibus.
*/prof* = Ficha dos professores.
          """
                            , parse_mode='Markdown')
        elif texto == 'oi':
            bot.sendMessage(chat_id, "Oi!!!")
        elif recebeComandoFotos(texto, msg):
            enviarFotosData(texto, msg, bot, chat_id)
        elif texto == '/listar':
            geraComandosFotos(bot, msg, chat_id)
        elif texto == '/onb':
            horaOnibus(bot, msg, chat_id)
        elif texto == '/prof':
            professor(bot, msg, chat_id)
        elif texto == "/uponb":
            FLAG = 1
            bot.sendMessage(chat_id, "Ok, me envie a foto!")
        elif texto == "/upprof":
            FLAG = 2
            bot.sendMessage(chat_id, "Ok, me envie a foto!")
        else:
            bot.sendMessage(chat_id, "Não sou esse tipo de bot.")
    elif content_type == 'photo':
        baixarFotos(bot, msg, chat_id, FLAG)
        FLAG = None if FLAG is not None else FLAG
    else:
        bot.sendMessage(chat_id, 'Você não tem autorização!!!')
        bot.sendMessage(chat_id, """
Caso queira testar, envie uma menssagem para 
@ColdMaster - Menino do designer e Banco de dados.
@Renanzx - Ué, Isso não vai funcionar, talvez funcione.
@lucasnasm - Read the docs



Orgulhosamente em fase beta!!!
"""
                        , parse_mode='Markdown')


if __name__ == "__main__":
    verifica_db()
    verifica_pastas()
    MessageLoop(bot, corpo).run_as_thread()
    print 'Rodando...'
    while 1:
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            fecha_conexao()
            exit(0)
