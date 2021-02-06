import telebot
from telebot import types
from match_info import get_all_team_matches, get_all_matches

bot = telebot.TeleBot('1338916573:AAEl8uBoXRxJY-xl1FiIlM1CIrFJFgKSbt4')


@bot.message_handler(content_types=['text'])
def start_message(message):
    answer = 'Добро пожаловать! Я бот, который расскажет вам о результатах матчей АПЛ'

    keyboard = types.InlineKeyboardMarkup()
    key_all_matches = types.InlineKeyboardButton(text='Все результаты', callback_data='all_matches')
    keyboard.add(key_all_matches)

    bot.send_message(message.chat.id, answer, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'all_matches':
        bot.send_message(call.from_user.id, get_all_team_matches('Arsenal'))


bot.polling(none_stop=True, interval=0)
