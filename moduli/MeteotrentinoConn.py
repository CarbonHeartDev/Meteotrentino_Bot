from urllib import request
import json

class MeteotrentinoConn:

    def __init__(self):
        temp = request.urlopen("https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)
        

    def aggiorna(self):
        temp = request.urlopen("https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)

    def richiedi(self,IDr,giorni_avanti):
        previsione = [self.dati["previsione"][IDr]["giorni"][giorni_avanti]["giorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["testoGiorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMinGiorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMaxGiorno"]]
        return previsione