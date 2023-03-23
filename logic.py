import telebot
from telebot import types

bot = telebot.TeleBot('5993898259:AAGwKzAM7IBnwM4rHo7OVoBI8-ufdM0A2qk')

@bot.message_handler(commands=['start'])
def main (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # створення нових кнопок
    btn1 = types.KeyboardButton('Запитання і відповіді')
    btn2 = types.KeyboardButton('Створити звернення')
    btn3 = types.KeyboardButton('Викликати менеджера')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, 'Оберіть те, що вас цікавить', reply_markup=markup)  # відповідь бота
    #if message.text == 'Запитання і відповіді':
    #    return FAQ(message)

#@bot.callback_query_handler(lambda c:c.text == "Запитання і відповіді")
#def send_button1(message: types.Message):
#@bot.message_handler(content_types=['text'])
# def FAQ(message):
#     if message.text == 'Запитання і відповіді':
#         print("555555", message.text)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Кешбек загубився/відхилився")
#         btn2 = types.KeyboardButton('Кешбек затримується')
#         btn3 = types.KeyboardButton('Вивід коштів')
#         btn4 = types.KeyboardButton('Технічні труднощі')
#         btn5 = types.KeyboardButton('Інші питання')
#         btn6 = types.KeyboardButton('Реферальна програма')
#         btn7 = types.KeyboardButton('Моніторинг цін')
#         btn8 = types.KeyboardButton('Викликати менеджера')
#         btn9 = types.KeyboardButton('Повернутись на початок')
#         markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
#         bot.send_message(message.from_user.id, f'Привіт, я твій особистий бот LetyShops!\n'
#                                                f'Обери своє питання', reply_markup=markup)
        #if message.text == 'Повернутись на початок':
            #return main(message)
        #elif message.text == 'Кешбек загубився/відхилився':
            #return cahback_denied(message)
            #bot.register_next_step_handler(message, cahback_denied)

@bot.message_handler(content_types=['text'])
def cahback_denied(message):
    if message.text == 'Запитання і відповіді':
        print("1?2?3", message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Чому кешбек загубився?')
    btn2 = types.KeyboardButton(text='Чому кешбек відхилився?')
    btn3 = types.KeyboardButton(text='Можливі причини втрати')
    btn4 = types.KeyboardButton(text='Що робити при втраті кешбеку?')
    btn5 = types.KeyboardButton(text='Як створити заявку/відкрити спір?')
    btn6 = types.KeyboardButton(text='Інше питання')
    btn7 = types.KeyboardButton(text='Повернутись')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.from_user.id, "Яке саме питання тебе цікавить?", reply_markup=markup)
    #if message.text == 'Чому кешбек загубився?':
        #return whylost(message)
        #bot.register_next_step_handler(message, whylost)
    #elif message.text == 'Повернутись':
        #return FAQ(message)

@bot.message_handler(content_types=['text'])
def whylost(message):
    print(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Створити заявку')
    btn2 = types.KeyboardButton(text='Повернутись')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, f'Насамперед перевір, скільки часу пройшло з моменту здійснення замовлення. В основному кешбек буде в особистому кабінеті протягом доби після оформлення замовлення, а в деяких магазинах упродовж декількох днів. Зазвичай ми публікуємо цю інформацію на сторінці магазину \n'
                                           f'\n' 
                                           f'При цьому іноді ми можемо не отримати від магазину кешбек за замовлення. Ось кілька основних причин, через які кешбек може не нарахуватись:\n'
                                           f'1. Перед замовленням не було зроблено перехід від LetyShops. Саме завдяки переходу магазин знає, що замовлення було зроблено від нас і готовий нарахувати кешбек.\n'
                                           f'2. Були порушені умови магазину. Вони відображені на сторінці кожного магазину в розділі "Інформація та умови". \n'
                                           f'3. Не були дотримані рекомендації щодо здійснення покупки з кешбеком та умов магазину.\n'
                                           f'4. Під час замовлення були включені сторонні розширення, які можуть перезаписувати партнерські посилання і привласнювати весь кешбек. Наприклад, Adblock, friGate CDN, Aliexpress Seller Check, VPN/Proxy/Socks і інші. Їх варто відключати під час здійснення покупки.\n'
                                           f'\n' 
                                           f'Якщо ти все зробив вірно, а кешбек загубився — створи заявку і додай необхідну інформацію про замовлення. Ми допоможемо вирішити це питання.\n', reply_markup=markup)
    #if message.text == 'Повернутись':
    #    return cahback_denied(message)

bot.polling(none_stop=True, interval=0)
