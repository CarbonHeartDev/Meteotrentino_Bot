import json

def predisponi(url):
    with open(url,'r',encoding='utf-8') as file:
        raw=file.read()
    return json.loads(raw)