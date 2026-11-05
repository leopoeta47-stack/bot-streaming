import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "9206087807:AAH1TV6rqaOcwnV7udbXEhoOP1FKK5LOR8w"

async def detectar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        texto = update.message.text.lower()
        usuario = update.message.from_user.first_name
        
        palabras_clave = [
            "netflix", "disney", "iptv", "magis", "magistv",
            "canva", "hbo", "hbo max", "amazon", "prime video"
        ]
        
        if any(palabra in texto for palabra in palabras_clave):
            respuesta = f"¡Hola {usuario}! 👋 Veo que estás preguntando por un servicio de streaming. Escríbeme a mi Telegram personal @LEOtreeckx para brindarte toda la información y precios."
            await update.message.reply_text(respuesta)

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), detectar_mensaje)
    application.add_handler(handler)
    
    print("Bot en línea y escuchando...")
    async with application:
        await application.start()
        await application.updater.start_polling()
        await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
