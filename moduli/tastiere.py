import telepot 
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

principale=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Previsioni della mia zona')],
    [KeyboardButton(text='Previsioni di un altra zona')],
    [KeyboardButton(text='Impostazioni')]
    ])

annulla=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='annulla')]])

impostazioni = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Cambia zona')],
    [KeyboardButton(text='Abbonamento')],
    [KeyboardButton(text='Cancella account')]
    ])


abbonamento = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='attiva')],
    [KeyboardButton(text='disattiva')],
    ])

conferma_cancellazione = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='cancella')],
    [KeyboardButton(text='non cancellare')],
    ])
