from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def make_standard_keyboard(buttons):
    return ReplyKeyboardMarkup(keyboard=buttons)


def make_inline_keyboard(buttons):
    for button in buttons:
        button = list(InlineKeyboardButton(text=button[0], callback_data=button[1]))
    return InlineKeyboardMarkup(inline_keyboard=buttons)
