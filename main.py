import requests
import random
import telebot
from bs4 import BeautifulSoup as bs
from moduls.setting import TOKEN

URL = 'https://www.anekdot.ru/last/good'

def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_anekdots = parser(URL)
random.shuffle(list_anekdots)

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Введите любую цифру')

@bot.message_handler(content_types=['text'])
def anekdots(message):
    if message.text.isdigit():
        bot.send_message(message.chat.id, list_anekdots[0])
        del list_anekdots[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру')

bot.polling()
