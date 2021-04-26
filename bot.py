from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup
import sqlite3



def echo(update, context):
    con = sqlite3.connect('db/users.db')
    cur = con.cursor()
    resultss = cur.execute(f"""SELECT * FROM users""").fetchall()
    tt = 0
    tr = 0
    fl = 0
    a, b = update.message.text.split()
    for el in resultss:
        if el[1] == str(a):
            if el[2] == str(b):
                tr = el[3]
                fl = el[4]
    update.message.reply_text(f'Верных {tr} Неверных{fl}')


def main():
    updater = Updater('1786659031:AAGA-uj8Nk8SOkzUlw0uMCldVZB9ZpE235A', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
