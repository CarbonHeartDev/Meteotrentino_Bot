from .prepare_json import prepare_json_file

class MessageMaker:

    def __init__(self,phrasesURL):
        self.phrases = prepare_json_file(phrasesURL)

    def prepare_daily_zone_forecast(self,municipality_name, days_ahead, language):
        retval = self.phrases[language]["send_forecast"]["zone_header"]%(municipality_name)
        retval += 
        return messagge
