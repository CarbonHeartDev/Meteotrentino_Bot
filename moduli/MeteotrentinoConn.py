from urllib import request
import json

class MeteotrentinoConn:

    def __init__(self):
        temp = request.urlopen("https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)
        

    def aggiorna(self):
        temp = request.urlopen("https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)

    def richiediSingola(self,IDr,giorni_avanti):
        temp = [self.dati["previsione"][IDr]["giorni"][giorni_avanti]["giorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["testoGiorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMinGiorno"],self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMaxGiorno"]]
        return temp

    def richiediTripla(self,IDr):
        temp = [self.richiediSingola(IDr,0),self.richiediSingola(IDr,1),self.richiediSingola(IDr,2)]
        return temp