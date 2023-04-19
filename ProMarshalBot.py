import telebot
from telebot.types import *
import marshal
import requests
import telebot
from telebot import types
TOKEN = "6282929370:AAGvHtTbPGMPoKc47SVW8jVEyHklUMp0Bl4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_inline(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    settings_button = types.InlineKeyboardButton(text='Developer 👨‍💻', url='https://t.me/pythonDevIoper')
    help_button = types.InlineKeyboardButton(text='👥 Group ➕', url='https://t.me/MarshalEncodingBot?startgroup=true')
    keyboard.add(settings_button, help_button)
    bot.send_message(message.chat.id, 'Asalomu aleykum 👋🏻\nFile 📁 sizning laringizni\nMarshal 👨‍💻 formatida </>\n🔐 encode qilib beruvchi\nBotga🤖 hush ☺️ kelibsiz 🚶\nYordam 🆘 kerak bolsa  /help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Encode 🔐  file 📁", callback_data='file')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Bot🤖 dan foydalanish 📠 uchun \npastagi tugmachani bosing', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button(call):
    
    if call.data == 'file':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'chunarli✓ menga file 📁 ni yuboring ⬆')

@bot.message_handler(content_types=['document'])
def custom(msg):
    FILE_ID = (msg.document.file_id)
    a = bot.get_file(file_id=FILE_ID).file_path
    b = bot.get_file_url(FILE_ID)
    
    if b[-2]+b[-1]=='py':
        x=bot.send_message(msg.chat.id,"Encoding time ⏳ ...")
        response = requests.get(b)
        data =compile(response.content,"marshal",'exec')
        redata = marshal.dumps(data)
        f = open("MarshalEnc.py", "w")
        f.write("#Encoded By @KgzNet\nimport marshal\nexec(marshal.loads("+str(redata)+"))")
        try:
            with open('MarshalEnc.py','rb') as f:
                bot.delete_message(msg.chat.id,x.message_id)
                bot.send_document(msg.chat.id,document=f)
        except Exception as e:
            print(e)
print(bot.get_me())
bot.infinity_polling()
