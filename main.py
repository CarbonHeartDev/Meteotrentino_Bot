import telepot
import time
from telepot.loop import MessageLoop
import moduli.keyboards as keyboards
from moduli.GestioneUtenti import GestioneUtenti
from moduli.predisponiJson import predisponi
from moduli.strumentiUrl import assoluta
from moduli.Geo import Geo
from moduli.MeteotrentinoConn import MeteotrentinoConn

HTTPtoken = ''
bot = telepot.Bot(HTTPtoken)

database=GestioneUtenti(assoluta('\\Dati\\Attivi\\utenti.json'), assoluta('\\Dati\\Attivi\\chiaviMonouso.json'))
frasi=predisponi(assoluta('\\Dati\\Archivio\\Frasi.json'))
comuni=Geo(assoluta('\\Dati\\Archivio\\ListaComuni.json'))

source = MeteotrentinoConn()

def rispondi(msg):
    content_type, chat_type, chat_id=telepot.glance(msg)
    if content_type=='text':
        if database.esiste(chat_id):
            if database.getSessione(chat_id)==-2:
                temp=comuni.cerca(msg['text'])
                if temp==-1:
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_errore"][1])
                else:
                    database.setComune(chat_id,comuni.pdi[temp]["nome"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["posizione_impostata"])
                    bot.sendMessage(chat_id,frasi["impostazioni"]["nome"])
                    database.setSessione(chat_id,-1)
            elif database.getSessione(chat_id)==-1:
                database.setNome(chat_id,msg['text'])
                database.setSessione(chat_id,0)
                bot.sendMessage(chat_id,frasi["impostazioni"]["completamento"])
            elif database.getSessione(chat_id)==0:
                bot.sendMessage(chat_id,frasi["principale"]%(database.getNome(chat_id)),reply_markup=keyboards.principale)

        else:
            bot.sendMessage(chat_id,frasi["impostazioni"]["saluto"])
            bot.sendMessage(chat_id,frasi["impostazioni"]["posizione"])
            database.inserisciUtente(chat_id,"null","null")


        
        

def pulsante(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    if query_data=='plocali':
        p0=source.richiedi(comuni.getIDr(database.getComune(chat_id)),0)
        p1=source.richiedi(comuni.getIDr(database.getComune(chat_id)),0)
        p2=source.richiedi(comuni.getIDr(database.getComune(chat_id)),0)
        bot.sendMessage(chat_id,frasi["invio_previsione"]["invia"]%database.getComune(chat_id)+frasi["invio_previsione"]["previsione_singola"]%(p0[0],p0[1],p0[2],p0[3]))
        


MessageLoop(bot, {'chat': rispondi, 'callback_query': pulsante}).run_as_thread()
print('Bot attivato')

while True:
    time.sleep(10)
