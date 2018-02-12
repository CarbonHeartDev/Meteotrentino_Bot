from os import sys
import time

import telepot
from telepot.loop import MessageLoop

from modules.keyboard_maker import make_inline_keyboard, make_standard_keyboard
from modules.users import UsersDatabase
from modules.prepare_json import prepare_json_file
from modules.file_url_helper import relative_to_absolute
from modules.point_of_interest_management import PointOfInterest
from modules.meteotrentino_connection import MeteotrentinoConnection
from modules.prepare_messages import prepare_text_weather_forecast_message

HTTPtoken = sys.argv[1]
bot = telepot.Bot(HTTPtoken)

database = UsersDatabase(relative_to_absolute('\\Data\\Users_Database\\users.json'),
                          relative_to_absolute('\\Data\\Users_database\\tokens.json'))
phrases = prepare_json_file(relative_to_absolute('\\Data\\Archive\\LOCALS.json'))
municipalities = PointOfInterest(relative_to_absolute('\\Data\\Archive\\MUNICIPALITIES.json'))

source = MeteotrentinoConnection()


def answer(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if database.check_if_exists(chat_id):
        if database.get_session(chat_id) == -2:
            if content_type == "text":
                temp = municipalities.search(msg['text'])
                if temp == -1:
                    bot.sendMessage(
                        chat_id, phrases["it"]["settings"]["posizion_error"][1])
                else:
                    database.set_municipality(chat_id, temp)
                    bot.sendMessage(
                        chat_id, phrases["it"]["settings"]["position_set"])
                    bot.sendMessage(chat_id, phrases["it"]["settings"]["name"])
                    database.set_session(chat_id, -1)
            if content_type == "location":
                temp = municipalities.near(msg["latitude"], msg["longitude"], 50)
                if temp == -1:
                    bot.sendMessage(
                        chat_id, phrases["it"]["settings"]["position_error"][0])
                else:
                    database.set_municipality(chat_id, temp)
                    bot.sendMessage(
                        chat_id, phrases["it"]["settings"]["position_set"])
                    bot.sendMessage(chat_id, phrases["it"]["settings"]["name"])
                    database.set_session(chat_id, -1)
        elif database.get_session(chat_id) == -1:
            if content_type == 'text':
                database.set_name(chat_id, msg['text'])
                database.set_session(chat_id, 0)
                bot.sendMessage(
                    chat_id, phrases["it"]["settings"]["first_boot_finish"])
            else:
                bot.sendMessage(chat_id, phrases["it"]["settings"]["name_error"])
        elif database.get_session(chat_id) == 0:
            bot.sendMessage(chat_id, phrases["it"]["main"] % (
                database.get_name(chat_id)), reply_markup=make_standard_keyboard(phrases["it"]["main_keyboard"]))
            if msg['text'] == "Previsioni della mia zona":
                bot.sendMessage(chat_id, prepare_text_weather_forecast_message(database.get_municipality(
                    chat_id), source.three_days_forecast(municipalities.getIDr(database.get_municipality(chat_id)))))
            if msg['text'] == "Previsioni di un altra zona":
                bot.sendMessage(
                    chat_id, "Per avere le posizioni di un altra zona inviami la tua posizione o digita il nome di un comune trentino.", reply_markup=make_standard_keyboard(phrases["it"]["back_button"]))
                database.set_session(chat_id, 1)
        elif database.get_session(chat_id) == 1:
            if content_type == "text":
                if msg['text'] != "annulla":
                    temp = municipalities.search(msg['text'])
                    if temp == -1:
                        bot.sendMessage(
                            chat_id, phrases["it"]["settings"]["position_error"][1])
                    else:
                        bot.sendMessage(chat_id, prepare_text_weather_forecast_message(temp, source.three_days_forecast(
                            municipalities.getIDr(temp))), reply_markup=make_standard_keyboard(phrases["it"]["main_keyboard"]))
                        database.set_session(chat_id, 0)
                else:
                    bot.sendMessage(
                        chat_id, "Ok, ritorno al menu principale.", reply_markup=make_standard_keyboard(phrases["it"]["main_keyboard"]))
                    database.set_session(chat_id, 0)
            if content_type == "location":
                print(msg)
                temp = municipalities.near(
                    msg["location"]["latitude"], msg["location"]["longitude"], 10000)
                if temp == -1:
                    bot.sendMessage(
                        chat_id, phrases["it"]["settings"]["position_error"][0])
                else:
                    bot.sendMessage(chat_id, prepare_text_weather_forecast_message(temp, source.three_days_forecast(
                        municipalities.getIDr(temp))), reply_markup=make_standard_keyboard(phrases["it"]["main_keyboard"]))
                    database.set_session(chat_id, 0)

    else:
        if content_type == "text":
            bot.sendMessage(chat_id, phrases["it"]["settings"]["first_message"])
            bot.sendMessage(chat_id, phrases["it"]["settings"]["first_boot_position"])
            database.new_user(chat_id, "null", "null")


MessageLoop(bot, {'chat': answer}).run_as_thread()
print('Bot attivato')

while True:
    time.sleep(10)
