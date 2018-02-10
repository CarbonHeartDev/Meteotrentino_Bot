from tinydb import TinyDB, Query
from tinydb.operations import delete,set
from random import randint

class GestioneUtenti:

    def __init__(self,jsonUtenti,jsonChiaviMonouso):
        self.utenti=jsonUtenti
        self.chiaviMonouso=jsonChiaviMonouso
        self.dbU=TinyDB(self.utenti)
        self.dbC=TinyDB(self.chiaviMonouso)

    def inserisciUtente(self,TgID,nome,comune):
        self.dbU.insert({'TgID':TgID,'nome':nome,'comune':comune,'sessione':-2,'stato_account':0})

    def esiste(self,TgID):
        utente = Query()
        return self.dbU.contains(utente.TgID == TgID)

    def prom(self,TgID,chiaveMonouso):
        chiave=Query()
        if(self.dbC.contains(chiave.chiave == chiaveMonouso)):
            self.dbC.update(delete('chiave'), chiave.chiave == chiaveMonouso)
            utente=Query()
            self.dbU.update(set('admin',1), utente.TgID == TgID)
            return True
        else:
            return False

    def getSessione(self,TgID):
        utente = Query()
        risultato = self.dbU.search(utente.TgID==TgID)
        return risultato[0]["sessione"]

    def setSessione(self,TgID,new_sessione):
        utente=Query()
        self.dbU.update(set('sessione',new_sessione), utente.TgID == TgID)
 
    def getComune(self,TgID):
        utente = Query()
        risultato = self.dbU.search(utente.TgID==TgID)
        return risultato[0]["comune"]
  
    def setComune(self,TgID,new_comune):
        utente=Query()
        self.dbU.update(set('comune',new_comune), utente.TgID == TgID)

    def getNome(self,TgID):
        utente = Query()
        risultato = self.dbU.search(utente.TgID==TgID)
        return risultato[0]["nome"]
  
    def setNome(self,TgID,new_nome):
        utente=Query()
        self.dbU.update(set('nome',new_nome), utente.TgID == TgID)

    def generaChiave(self):
        q=Query()
        while True:
            codice=randint(100000,999999)
            if(self.dbC.contains(q.chiave == codice)):
                break
        self.dbC.insert({'chiave':codice})

