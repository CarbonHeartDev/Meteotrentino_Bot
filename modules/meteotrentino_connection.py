from urllib import request
import json

from .point_of_interest_management import search, near
from .file_url_helper import relative_to_absolute


class MeteotrentinoConnection:

    def __init__(self):
        temp = request.urlopen(
            "https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)
        self.municipalities = PointOfInterest(relative_to_absolute('\\Data\\Archive\\MUNICIPALITIES.json'))


    def update(self):
        temp = request.urlopen(
            "https://www.meteotrentino.it/protcivtn-meteo/api/front/previsioneOpenDataLocalita")
        self.dati = json.load(temp)

    def regionwide_forecast(self):
        return self.dati["evoluzioneBreve"]

    def zone_forecast(self, municipality, days_ahead):
        IDr = self.municipalities.getIDr(municipality)
        retval = {"day":self.dati["previsione"][IDr]["giorni"][giorni_avanti]["giorno"],"data": list()}
        for fascia in self.dati["previsione"][IDr]["giorni"][giorni_avanti]["fasce"]:
            retval.data.append([fascia["fasciaPer"],fascia["fasciaOre"],fascia["descIcona"]])
        return temp

    def search_station_from_string(self, query):
        retval = search(query)
        return retval

    def search_station_from_GPS(self, lat, lon):
        retval = near(lat, lon, 50)
        return retval
