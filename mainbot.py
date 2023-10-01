import telebot
from telebot import TeleBot
from telebot import types
import peewee as pw

token = '2107353516:AAG5rWcJ7uYmzU0-UnBtScqCMiaeVKVSlwM'
bot = telebot.TeleBot(token)


connection = pw.MySQLDatabase('apteki', host='localhost', port=3306, user='root', passwd='')
connection.connect()

class lekarstva(pw.Model):
  name         = pw.TextField()
  price        = pw.IntegerField()
  instockornot = pw.IntegerField()
  adress       = pw.TextField()
  country      = pw.TextField()
  site         = pw.TextField()
  class Meta:
    database = connection

          #Начальное сообщение
@bot.message_handler(commands=['start'])

def start_message(message):
          #Создаем кнопки

  keyboard = telebot.types.ReplyKeyboardMarkup(True)
  keyboard.row('Помощь')

          #Приветственное сообщение
  bot.send_message(message.chat.id, 'Здравствуйте, вас приветствует Бот-аптека!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def send_text(message):
  
          #Поиск лекарств
  if message.text == 'Помощь':
    bot.send_message(message.chat.id, 'Для того, чтобы найти лекарство, введите его название в чат. \n')
    
  if len(message.text) < 3:
    bot.send_message(message.chat.id, '❌Вы ввели слишком короткий запрос')

  else: 
    bot.send_message(message.chat.id, 'Выполняю поиск')

          #Запрос в БД
    search = ('%' + message.text + '%').lower()
    test   = lekarstva.select().where((lekarstva.name % search) & (lekarstva.instockornot == 1)).order_by(lekarstva.price.asc())#.get()
    #result = connection.execute(test)
    a = 0
    for medObj in test:
      bot.send_message(message.chat.id, '💊Название товара: ' + medObj.name + '\n \n 💸Цена товара: ' + str(medObj.price) + ' руб. \n 🌐Сайт товара: ' + medObj.adress + '\n 🗺Производитель: ' + medObj.country + '\n 🔗Ссылка на товар: ' + medObj.site)
      a+=1
      if a >= 3: 
        break

bot.infinity_polling()