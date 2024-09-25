import qrcode.constants
import telebot
import qrcode
from io import BytesIO
from telebot import types
from forward import API_TOKEN
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def startfunc(message):
    bot.send_message(message.chat.id,"Assalom alaaykum Xush kelibsiz !!!")


@bot.message_handler(func=lambda message: True)
def messagefunc(message):
    text = message.text
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black",back_color = "white")

    buf = BytesIO()
    img.save(buf)
    buf.seek(0)

    bot.send_photo(message.chat.id,buf)

bot.polling(none_stop=True)
