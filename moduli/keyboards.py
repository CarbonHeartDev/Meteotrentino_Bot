import telepot 
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

principale=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Previsioni della mia zona', callback_data='plocali')],
    [InlineKeyboardButton(text='Previsioni di un altra zona', callback_data='pesterne')],
    [InlineKeyboardButton(text='Impostazioni', callback_data='impostazioni')]
    ])

impostazioni = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Cambia zona', callback_data='czona')],
    [InlineKeyboardButton(text='Abbonamento', callback_data='abbonamento')],
    [InlineKeyboardButton(text='Cancella account', callback_data='cancella')]
    ])


abbonamento = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='attiva', callback_data='attiva_abb')],
    [InlineKeyboardButton(text='disattiva', callback_data='disattiva_abb')],
    ])

conferma_cancellazione = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='cancella', callback_data='conferma_cancellazione')],
    [InlineKeyboardButton(text='non cancellare', callback_data='non_cancellare')],
    ])
