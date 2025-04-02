import telebot
from telebot import types
import os
import main


TOKEN = '7676992182:AAEzs9LIeNw2qvj8taqEcRx86v0TNgRA2YE'


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    # Приветственное сообщение
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1 класс")
    btn2 = types.KeyboardButton("2-3 класс")
    btn3 = types.KeyboardButton("4-5 класс")
    btn4 = types.KeyboardButton("6-7 класс")
    btn5 = types.KeyboardButton("8-11 класс")
    btn_back = types.KeyboardButton("Назад")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn_back)
    bot.send_message(message.chat.id, "Привет! Выберите возрастную категорию учащихся:", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text in ["1 класс", "2-3 класс", "4-5 класс", '6-7 класс', '8-11 класс'])
def age_category(message):
    age_category = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton("Назад")
    markup.add(btn_back)

    bot.send_message(message.chat.id, f"Вы выбрали возрастную категорию: {age_category}. Теперь загрузите файл Excel.",
                     reply_markup=markup)

    bot.register_next_step_handler(message, handle_excel_upload, age_category)



@bot.message_handler(func=lambda message: message.text == "Назад")
def back_to_age_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1 класс")
    btn2 = types.KeyboardButton("2-3 класс")
    btn3 = types.KeyboardButton("4-5 класс")
    btn4 = types.KeyboardButton("6-7 класс")
    btn5 = types.KeyboardButton("8-11 класс")
    btn_back = types.KeyboardButton("Назад")


    markup.add(btn1, btn2, btn3, btn4, btn5, btn_back)
    bot.send_message(message.chat.id, "Выберите возрастную категорию учащихся:", reply_markup=markup)



def handle_excel_upload(message, age_category):
    try:
        if message.document:
            # Получаем файл
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Сохраняем файл временно
            with open("uploaded_file.xlsx", 'wb') as new_file:
                new_file.write(downloaded_file)
            df, sp = main.action("uploaded_file.xlsx", age_category)
            if len(sp) != 0:
                mess = 'Эти люди встречаются есть в групповой диагностие, но их нет в индивиудальной: ' + ', '.join(sp)
            else:
                mess = 'Все ученики найдены.'
            df.to_excel("uploaded_file_with_new_sheet.xlsx", index=False)

            # Отправляем обратно пользователю измененный файл
            with open("uploaded_file_with_new_sheet.xlsx", 'rb') as file:
                bot.send_document(message.chat.id, file, caption=f"Вот ваш обновленный файл с добавленным листом. \n" + mess)

            # Удаляем временные файлы
            os.remove("uploaded_file.xlsx")
            os.remove("uploaded_file_with_new_sheet.xlsx")

        else:
            bot.send_message(message.chat.id, "Пожалуйста, загрузите файл Excel.")
            bot.register_next_step_handler(message, handle_excel_upload, age_category)
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 класс")
        btn2 = types.KeyboardButton("2-3 класс")
        btn3 = types.KeyboardButton("4-5 класс")
        btn4 = types.KeyboardButton("6-7 класс")
        btn5 = types.KeyboardButton("8-11 класс")
        btn_back = types.KeyboardButton("Назад")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn_back)
        bot.send_message(message.chat.id, "Проблема какая-то...скорее всего какие-то мусорные данные в таблице...ну или класс не тот...", reply_markup=markup)



bot.polling(none_stop=True)
