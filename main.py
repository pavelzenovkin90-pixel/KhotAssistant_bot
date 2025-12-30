import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот KhotAssistant запущен!")

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg:
        await context.bot.send_message(chat_id=CHANNEL_ID, text=msg.text)
        await msg.reply_text("Сообщение отправлено!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_message))
    app.run_polling()

if __name__ == "__main__":
    main()
