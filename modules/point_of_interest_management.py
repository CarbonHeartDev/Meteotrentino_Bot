from math import sin, cos, sqrt, atan2, radians

from .prepare_json import prepare_json_file
from .search_help import town_name_compare


def _distAB(latA, lonA, latB, lonB):
    R = 6373.0
    dlon = lonB - lonA
    dlat = latB - latA
    a = sin(dlat / 2)**2 + cos(latA) * cos(latB) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


class PointOfInterest:
    def __init__(self, PDIlist):
        self.poi = prepare_json_file(PDIlist)

    def near(self, lat, lon, max):
        minD = max
        result = ""
        for val in self.poi:
            print(distAB(lat, lon, val["latitude"], val["longitude"]))
            if distAB(lat, lon, val["latitude"], val["longitude"]) < minD:
                minD = distAB(lat, lon, val["latitude"], val["longitude"])
                result = val["name"]
            i += 1
        print(minD)
        if minD == max:
            result = -1
        return result

    def search(self, target):
        i = 0
        retval = -1
        while (i < len(self.poi) and retval==-1):
            if town_name_compare(target, self.poi[i]["name"]):
                retval = self.poi[i]["name"]
            else:
                i += 1
        return retval

    def getIDr(self, name):
        i = 0
        retval = -1
        while (i < len(self.poi) and retval==-1):
            if self.poi[i]["name"]==name:
                retval = self.poi[i]["IDr"]
            else:
                i += 1
        return retval
