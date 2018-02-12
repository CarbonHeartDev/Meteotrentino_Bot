from urllib import request
import json


class MeteotrentinoConnection:

    def __init__(self):
        temp = request.urlopen(
            "https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)

    def update(self):
        temp = request.urlopen(
            "https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)

    def single_day_forecast(self, IDr, giorni_avanti):
        temp = [self.dati["previsione"][IDr]["giorni"][giorni_avanti]["giorno"], self.dati["previsione"][IDr]["giorni"][giorni_avanti]["testoGiorno"],
                self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMinGiorno"], self.dati["previsione"][IDr]["giorni"][giorni_avanti]["tMaxGiorno"]]
        return temp

    def three_days_forecast(self, IDr):
        temp = [self.single_day_forecast(IDr, 0), self.single_day_forecast(
            IDr, 1), self.single_day_forecast(IDr, 2)]
        return temp
