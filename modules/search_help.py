import re

from unidecode import unidecode


def town_name_compare(ori, des):
    ori = ori.lower()
    ori = unidecode(ori)
    ori = ori.replace("'", "[ ,']")
    des = des.lower()
    des = unidecode(des)
    if re.match('.*' + ori + '.*', des):
        return True
    else:
        return False
