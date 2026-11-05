import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "9206087807:AAHlTV6rqaOcwnV7udbXEhoOP1FKK5LOR8w"

async def detectar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        texto = update.message.text.lower()
        usuario = update.message.from_user.first_name
        
        palabras_clave = [
            "netflix", "disney", "iptv", "magis", "magistv", 
            "canva", "hbo", "hbo max", "amazon", "prime video"
        ]
        
        if any(palabra in texto for palabra in palabras_clave):
            respuesta = f"Hola {usuario}! 👋 Veo que estás preguntando por un servicio streaming. Escríbeme un mensaje al privado: @LEOtreeckx"
            await update.message.reply_text(respuesta)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), detectar_mensaje)
    application.add_handler(handler)
    
    print("Bot en línea y escuchando...")
    application.run_polling()
