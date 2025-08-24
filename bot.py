from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN
from utils.usda_api import search_food

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        " Hi! Send /food <name> to get nutritional info.\nExample: /food apple"
    )

async def food(update: Update, context : ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("" \
        "Please provide a food name. Example /food apple"
        )
        return
    
    query = " ".join(context.args)
    result = search_food(query=query)

    if not result:
        await update.message.reply_text(f"No result found for /food {query}")
        return
    
    text = f"*{result['description']}* 100g (FDC ID : {result['fdcId']})\n\n"

    for name, val in result["nutrients"].items():
        text+= f" - {name}: {val}\n"

    await update.message.reply_text(text, parse_mode="Markdown")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("food", food))

    print("Bot is running....")
    app.run_polling()

if __name__ == "__main__":
    main()
