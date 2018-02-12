import telepot
import time
from telepot.loop import MessageLoop
import moduli.tastiere as tastiere
from moduli.GestioneUtenti import GestioneUtenti
from moduli.predisponiJson import predisponi
from moduli.strumentiUrl import assoluta
from moduli.Geo import Geo
from moduli.MeteotrentinoConn import MeteotrentinoConn
from os import sys
from moduli.predisponiMessaggio import predisponiMessaggio

HTTPtoken = sys.argv[1]
bot = telepot.Bot(HTTPtoken)

database=GestioneUtenti(assoluta('\\Dati\\Attivi\\utenti.json'), assoluta('\\Dati\\Attivi\\chiaviMonouso.json'))
frasi=predisponi(assoluta('\\Dati\\Archivio\\Frasi.json'))
comuni=Geo(assoluta('\\Dati\\Archivio\\ListaComuni.json'))

source = MeteotrentinoConn()

def rispondi(msg):
    content_type, chat_type, chat_id=telepot.glance(msg)
    if database.esiste(chat_id):
        if database.getSessione(chat_id)==-2:
            if content_type=="text":
                temp=comuni.cerca(msg['text'])
                if temp==-1:
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_errore"][1])
                else:
                    database.setComune(chat_id,comuni.pdi[temp]["nome"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_impostata"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["nome"])
                    database.setSessione(chat_id,-1)
            if content_type=="location":
                temp=comuni.vicino(msg["latitude"],msg["longitude"],50)
                if temp==-1:
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_errore"][0])
                else:
                    database.setComune(chat_id,comuni.pdi[temp]["nome"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_impostata"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["nome"])
                    database.setSessione(chat_id,-1)
        elif database.getSessione(chat_id)==-1:
            if content_type=='text':
                database.setNome(chat_id,msg['text'])
                database.setSessione(chat_id,0)
                bot.sendMessage(chat_id,frasi["impostazioni"]["completamento"])
            else:
                bot.sendMessage(chat_id,frasi["impostazioni"]["nome_errore"])
        elif database.getSessione(chat_id)==0:
            bot.sendMessage(chat_id,frasi["principale"]%(database.getNome(chat_id)),reply_markup=tastiere.principale)
            if msg['text']=="Previsioni della mia zona":
                bot.sendMessage(chat_id,predisponiMessaggio(database.getComune(chat_id),source.richiediTripla(comuni.getIDr(database.getComune(chat_id)))))
            if msg['text']=="Previsioni di un altra zona":
                bot.sendMessage(chat_id,"Per avere le posizioni di un altra zona inviami la tua posizione o digita il nome di un comune trentino.",reply_markup=tastiere.annulla)
                database.setSessione(chat_id,1)
        elif database.getSessione(chat_id)==1:
            if content_type=="text":
                if msg['text']!="annulla":
                    temp=comuni.cerca(msg['text'])
                    if temp==-1:
                        bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_errore"][1])
                    else:
                        bot.sendMessage(chat_id,predisponiMessaggio(comuni.pdi[temp]["nome"],source.richiediTripla(comuni.getIDr(comuni.pdi[temp]["nome"]))),reply_markup=tastiere.principale)
                        database.setSessione(chat_id,0)
                else:
                    bot.sendMessage(chat_id,"Ok, ritorno al menu principale.",reply_markup=tastiere.principale)                
                    database.setSessione(chat_id,0)
            if content_type=="location":
                print(msg)
                temp=comuni.vicino(msg["location"]["latitude"],msg["location"]["longitude"],10000)
                if temp==-1:
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_errore"][0])
                else:
                    bot.sendMessage(chat_id,predisponiMessaggio(comuni.pdi[temp]["nome"],source.richiediTripla(comuni.getIDr(comuni.pdi[temp]["nome"]))),reply_markup=tastiere.principale)
                    database.setSessione(chat_id,0)


    else:
        if content_type=="text":
            bot.sendMessage(chat_id,frasi["impostazioni"]["saluto"])
            bot.sendMessage(chat_id,frasi["impostazioni"]["posizione"])
            database.inserisciUtente(chat_id,"null","null")

MessageLoop(bot, {'chat': rispondi}).run_as_thread()
print('Bot attivato')

while True:
    time.sleep(10)