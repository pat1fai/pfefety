import os
import telebot
import schedule
import time
from telegram.ext import Updater
from time import sleep
from telebot import types

username = os.getlogin()

telegram_token = '6503308325:AAFIihXV3N7WJizZnmBvrTgrD72CanhKlsE'

bot = telebot.TeleBot(telegram_token)

keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button1 = types.KeyboardButton("📅 Расписание")
button8 = types.KeyboardButton("⏰ Перемены")
button9 = types.KeyboardButton("❓ Информация")
button10 = types.KeyboardButton("📒 Последние Обновления")
keyboard.add(button1, button8, button9, button10)

schedule_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button2 = types.KeyboardButton("Понедельник")
button3 = types.KeyboardButton("Вторник")
button4 = types.KeyboardButton("Среда")
button5 = types.KeyboardButton("Четверг")
button6 = types.KeyboardButton("Пятница")
button7 = types.KeyboardButton("🔙 Назад")
schedule_keyboard.add(button2, button3, button4, button5, button6, button7)

time_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
time_keyboard.add(button7)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите:", reply_markup=keyboard)
    user_name = message.from_user.username
    print(f"Пользователь {user_name} написал команду /start")

@bot.message_handler(func=lambda message: message.text == "📅 Расписание")
def schedule(message):
    bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=schedule_keyboard)

@bot.message_handler(func=lambda message: message.text in ["Понедельник"])
def show_schedule(message):
    day = message.text
    bot.send_message(message.chat.id, f"Расписание на Понедельник (В Школе):\n\n1. -\n2. -\n3. -\n4. Укр. мова (307)\n5. Англ. мова (307)\n6. Укр. мова\n7. Укр. літ\n8. Заруб. літ\n9. Фізика")

@bot.message_handler(func=lambda message: message.text in ["Вторник"])
def show_schedule(message):
    day = message.text
    bot.send_message(message.chat.id, f"Расписание на Вторник (В Школе):\n\n1. -\n2. -\n3. -\n4. Алгебра (307)\n5. Геометрія\n6. Географія\n7. Біологія\n8. Історія\n9. Мистецтво")

@bot.message_handler(func=lambda message: message.text in ["Среда"])
def show_schedule(message):
    day = message.text
    bot.send_message(message.chat.id, f"Расписание на Среду (В Школе):\n\n1. -\n2. -\n3. -\n4. Хімія (307)\n5. Алгебра\n6. Фізика\n7. Основи правознавста\n8. Геометрія\n9. Основи здоров’я")

@bot.message_handler(func=lambda message: message.text in ["Пятница"])
def show_schedule(message):
    day = message.text
    bot.send_message(message.chat.id, f"Расписание на Пятницу (Дома):\n\n1. -\n2. Трудове навчання\n3. Англійська мова\n4. Українська література\n5. Фізична культура\n6. Зарубіжна література\n7. Хімія\n8. -\n9. -")

@bot.message_handler(func=lambda message: message.text in ["Четверг"])
def show_schedule(message):
    day = message.text
    bot.send_message(message.chat.id, f"Расписание на Четверг (Дома):\n\n1. Фізика\n2. Інформатика\n3. Біологія\n4. Німецька мова\n5. Німецька мова\n6. Всесвітня історія\n7. Фізична культура\n8. -\n9. -")

@bot.message_handler(func=lambda message: message.text == "⏰ Перемены")
def schedule(message):
    bot.send_message(message.chat.id, "1. 8.00 - 8.45\n2. 8.55 - 9.40\n3. 9.50 - 10.35\n4. 10.45 - 11.30\n5. 11.40 - 12.25\n6. 12.35 - 13.20\n7. 13.30 - 14.15\n8. 14.25 - 15.10\n9. 15.20 - 16.05", reply_markup=time_keyboard)


@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def go_back(message):
    bot.send_message(message.chat.id, "Выберите:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "❓ Информация")
def schedule(message):
    bot.send_message(message.chat.id, "Последнее Обновление Информации: 19.09\n\nПотверждённые расписания:\n\nПонедельник: ✅\nВторник: ✅\nСреда: ✅\nЧетверг: ✅\nПятница: ✅\n\nПоследнее Обновление Бота: 25.09\n\nСоздатели: @hadkikido", reply_markup=time_keyboard)

@bot.message_handler(func=lambda message: message.text == "📒 Последние Обновления")
def schedule(message):
    bot.send_message(message.chat.id, "Обновление 25.09:\n\n- adding a button logs\n- fixed unplanned shutdown of the bot after a while\n- adding a line about the latest bot update", reply_markup=time_keyboard)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)