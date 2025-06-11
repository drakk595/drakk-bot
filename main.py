import telebot as tg
from telebot import types

bot = tg.TeleBot('8167277256:AAECknCVYhGWb-wpSXx18w0sRdXuqRVqLJQ')

@bot.message_handler(commands=['start'])
def main(ms):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.ReplyKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('цены', callback_data='cen')
    btn2 = types.InlineKeyboardButton('подробнее', callback_data='pod')
    btn3 = types.InlineKeyboardButton('контакты', callback_data='kon')
    btn_restart = types.KeyboardButton('перезапустить')
    markup2.add(btn_restart)

    markup.row(btn3, btn2)
    markup.row(btn1)

    name = ms.from_user.first_name

    gif = open('gif.gif', 'rb')
    bot.send_animation(ms.chat.id, gif, reply_markup=markup2)
    bot.send_message(ms.chat.id, f'привет {name} ! ты попал в бот там где можно узнать информацию о покупке ботов😉.', reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def main(callback):
    if callback.data == 'cen':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('назад', callback_data='naz'))
        bot.send_message(callback.message.chat.id, 'цены варьируеться по сложности самого бота, начиная от 250грн(простые боты) и с подключением базы данных от 650грн', reply_markup=markup)
    elif callback.data == 'naz':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('цены', callback_data='cen')
        btn2 = types.InlineKeyboardButton('подробнее', callback_data='pod')
        btn3 = types.InlineKeyboardButton('контакты', callback_data='kon')

        markup.row(btn3, btn2)
        markup.row(btn1)

        name = callback.message.from_user.first_name

        bot.send_message(callback.message.chat.id, f'привет {name} ! ты попал в бот там где можно узнать информацию о покупке ботов😉.', reply_markup=markup)
    elif callback.data == 'pod':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('назад', callback_data='naz'))
        bot.send_message(callback.message.chat.id, 'данный бот создан человеком @drakktg, чтоб показать как пример / узнать куда писать для заказа', reply_markup=markup)
    elif callback.data == 'kon':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('назад', callback_data='naz'))
        bot.send_message(callback.message.chat.id, 'телеграм: @drakktg\nпока что большу нету...', reply_markup=markup)

@bot.message_handler()
def main(ms):
    if ms.text.strip().lower() == 'перезапустить':
        markup = types.InlineKeyboardMarkup()
        markup2 = types.ReplyKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('цены', callback_data='cen')
        btn2 = types.InlineKeyboardButton('подробнее', callback_data='pod')
        btn3 = types.InlineKeyboardButton('контакты', callback_data='kon')
        btn_restart = types.KeyboardButton('перезапустить бота' )
        markup2.add(btn_restart)

        markup.row(btn3, btn2)
        markup.row(btn1)

        name = ms.from_user.first_name

        gif = open('gif.gif', 'rb')
        bot.send_animation(ms.chat.id, gif, reply_markup=markup2)
        bot.send_message(ms.chat.id, f'привет {name} ! ты попал в бот там где можно узнать информацию о покупке ботов😉.', reply_markup=markup)

if __name__ == '__main__':
    bot.infinity_polling()