from .predisponiJson import predisponi
from math import sin, cos, sqrt, atan2, radians
from .aiuto_ricerca import compara

def distAB(latA,lonA,latB,lonB):
    R = 6373.0
    dlon = lonB - lonA
    dlat = latB - latA
    a = sin(dlat / 2)**2 + cos(latA) * cos(latB) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

class Geo:
    def __init__(self,listaPDI):
        self.pdi=predisponi(listaPDI)

    def vicino(self, lat, lon, max):
        minD=max
        minI=-1
        i=0
        for val in self.pdi:
            print(distAB(lat,lon,val["latitudine"],val["longitudine"]))
            if distAB(lat,lon,val["latitudine"],val["longitudine"]) < minD:
                minD=distAB(lat,lon,val["latitudine"],val["longitudine"])
                minI=i
            i+=1
        print(minD)
        if minD==max:
            minI=-1
        return minI

    def cerca(self, ricerca):
        i=0
        print(len(self.pdi))
        while i<len(self.pdi):
            print(compara(ricerca,self.pdi[i]["nome"]))
            if compara(ricerca,self.pdi[i]["nome"]):
                return i
            else:
                i+=1
        return -1
    
    def getIDr(self, nome):
        i=0
        while self.pdi[i]["nome"]!=nome:
            i+=1
        return self.pdi[i]["IDr"]

    
