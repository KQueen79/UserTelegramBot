from datetime import datetime, timedelta
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

musica_actual = {}

# Función para generar un enlace de descarga
def generar_enlace_descarga(nombre_cancion):
    # Asumimos que los archivos mp3 están alojados en un servidor accesible
    base_url = "https://tu-servidor.com/descargas/"
    enlace = f"{base_url}{nombre_cancion.replace(' ', '%20')}.mp3"
    return enlace

# Comando de inicio
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot de administración. Usa el comando /musica para compartir la música que estás escuchando.')

# Comando para compartir música
async def musica(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name
    message_text = update.message.text.split(' ', 1)
    if len(message_text) > 1:
        musica_actual[user_id] = {
            "musica": message_text[1],
            "timestamp": datetime.now()
        }
        enlace_descarga = generar_enlace_descarga(message_text[1])
        await update.message.reply_text(f'¡Genial! Ahora todos saben que estás escuchando: {message_text[1]}\nPuedes descargarla aquí: [Descargar]({enlace_descarga})')
        await context.bot.send_message(chat_id='@CMenvivo', text=f'{user_name} está escuchando: {message_text[1]}\nPuedes descargarla aquí: [Descargar]({enlace_descarga})')
    else:
        await update.message.reply_text('Por favor, incluye el nombre de la canción que estás escuchando. Ejemplo: /musica [nombre de la canción]')

# Comando para mostrar la música actual de todos
async def mostrar_musica(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    respuesta = "Aquí está la música que los usuarios están escuchando actualmente:\n"
    for user_id, info in musica_actual.items():
        if datetime.now() - info['timestamp'] < timedelta(hours=24):
            enlace_descarga = generar_enlace_descarga(info['musica'])
            respuesta += f"ID: {user_id}, Música: {info['musica']} - [Descargar]({enlace_descarga})\n"
    if len(musica_actual) == 0:
        respuesta = "No hay música compartida en las últimas 24 horas."
    await update.message.reply_text(respuesta)

def main() -> None:
    application = ApplicationBuilder().token("7250794654:AAF5vW_My4QEfmuTpp6YOYsC1RyrbhX205o").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("musica", musica))
    application.add_handler(CommandHandler("mostrar_musica", mostrar_musica))

    application.run_polling()

if __name__ == "__main__":
    main()
