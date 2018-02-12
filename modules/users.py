from random import randint

from tinydb import TinyDB, Query
from tinydb.operations import delete, set


class UsersDatabase:

    def __init__(self, jsonUtenti, jsonChiaviMonouso):
        self.users = jsonUtenti
        self.tokens = jsonChiaviMonouso
        self.dbU = TinyDB(self.users)
        self.dbC = TinyDB(self.tokens)

    def new_user(self, TgID, name, municipality):
        self.dbU.insert({'TgID': TgID, 'name': name,
                         'municipality': municipality,
                         'session': -2, 'account_status': 0,
                         'days_from_last_access': 0, 'attempts': 3})

    def check_if_exists(self, TgID):
        user = Query()
        return self.dbU.contains(user.TgID == TgID)


    def prom(self, TgID, token):
        record = Query()
        current = self.dbU.search(user.TgID == TgID)
        retval=-1
        if current[0]["attempts"]!=0:
            if(self.dbC.contains(record.token == token)):
                self.dbC.update(delete('token'), token.chiave == token)
                user = Query()
                self.dbU.update(set('account_status', 1), user.TgID == TgID)
                retval=True
            else:
                self.dbU.update(set('attempts', current[0]["attempts"]), user.TgID == TgID)
                if current[0]["attempts"]==1:
                    self.dbU.update(set('account_status', -1), user.TgID == TgID)                
                retval = current[0]["attempts"]-1
        return retval

    def get_session(self, TgID):
        user = Query()
        result = self.dbU.search(user.TgID == TgID)
        return result[0]["session"]

    def set_session(self, TgID, new_session):
        user = Query()
        self.dbU.update(set('session', new_session), user.TgID == TgID)

    def get_municipality(self, TgID):
        utente = Query()
        risultato = self.dbU.search(utente.TgID == TgID)
        return risultato[0]["municipality"]

    def set_municipality(self, TgID, new_municipality):
        user = Query()
        self.dbU.update(set('municipality', new_municipality),
                        user.TgID == TgID)

    def get_name(self, TgID):
        utente = Query()
        risultato = self.dbU.search(utente.TgID == TgID)
        return risultato[0]["name"]

    def set_name(self, TgID, new_nome):
        user = Query()
        self.dbU.update(set('name', new_nome), user.TgID == TgID)

    def generate_new_key(self):
        record = Query()
        while True:
            codice = randint(100000, 999999)
            if(self.dbC.contains(record.token == codice)):
                break
        self.dbC.insert({'token': codice})
