# encoding: utf-8
import sys
import time
import telepot
from telepot.loop import MessageLoop
from funcoes import *

#Token do @assisbeta_bot, não precisa setar via linha de comando
#token apagado por questões de privacidade
TOKEN = ""
bot = telepot.Bot(TOKEN)
#funcao corpo
def corpo(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #ids de usuarios com permissões, aleatorios por questões de privacidade
    usu=[111111,213213213,213213]
    ids = msg['from']['id']
    debugMenssagens(content_type,msg)
    if (content_type == 'text') and  (ids in usu):
        
        texto = msg['text'].lower()
        recebe_comandos = str(recebeComandoFotos(texto,msg))
        if texto == '/start':
          bot.sendMessage(chat_id,"""
Bem vindo calouro, me chamo AssiS, e os meus comandos são os seguintes:

*/listar* = Fotos que firam salvas.
*/onb* = Horário do onibus.
*/prof* = Ficha dos professores.
          """
          ,parse_mode='Markdown')
        elif texto == 'oi':
            bot.sendMessage(chat_id, "Oi!!!")
        elif str(texto[1:]) == recebe_comandos:
            enviarFotosData(texto,msg,bot,chat_id)
        elif texto == '/listar':
            geraComandosFotos(bot,msg,chat_id)
        elif texto == '/onb':
            horaOnibus(bot,msg,chat_id)
        elif texto == '/prof':
            professor(bot,msg,chat_id)
        else:
            bot.sendMessage(chat_id,"Não sou esse tipo de bot.")
          
    elif content_type == 'photo':
        baixarFotos(bot,msg,chat_id)
    else:
        bot.sendMessage(chat_id,'Você não tem autorização!!!')
        bot.sendMessage(chat_id, """
Caso queira testar, envie uma menssagem para 
@ColdMaster - Menino do designer e Banco de dados.
@Renanzx - Ué, Isso não vai funcionar, talvez funcione.
@lucasnasm - Read the docs



Orgulhosamente em fase beta!!!
"""
,parse_mode='Markdown')



MessageLoop(bot, corpo).run_as_thread()
print 'Rodando...'

# as linhas abaixo irao deixar o codigo rodando num loop
# Keep the program running.
while 1:
    time.sleep(10)

