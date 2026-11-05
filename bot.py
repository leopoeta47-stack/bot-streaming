import os
import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "9206087807:AAHlTV6rqaOcwnV7udbXEhOoP1FKK5L0R8w"

# Servidor HTTP simple para que Render reconozca el Web Service
async def handle_ping(request):
    return web.Response(text="Bot activo 24/7")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

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
    # Inicia el servidor web interno para Render
    await start_web_server()
    
    # Inicia el bot de Telegram
    application = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), detectar_mensaje)
    application.add_handler(handler)
    
    async with application:
        await application.start()
        await application.updater.start_polling()
        print("Bot en línea y servidor listo...")
        await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
