from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = "8669166205:AAElxk-2ANvvz53EY-naM2OzF21n632ktQg"
OWNER = "https://t.me/Rynlox"

async def start(update, context):

    keyboard = [
        [InlineKeyboardButton("📍 Власник", url=OWNER)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚠️ Аккаунт під контролем системи: fTvY1",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
