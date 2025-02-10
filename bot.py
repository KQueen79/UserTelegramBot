from datetime import datetime, timedelta
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from cryptography.fernet import Fernet

# Generar una clave de encriptación
key = Fernet.generate_key()
cipher_suite = Fernet(key)

suscriptores_activos = {}
musica_actual = {}

# Función para generar un enlace de descarga
def generar_enlace_descarga(nombre_cancion):
    # Asumimos que los archivos mp3 están alojados en un servidor accesible
    base_url = "https://tu-servidor.com/descargas/"
    enlace = f"{base_url}{nombre_cancion.replace(' ', '%20')}.mp3"
    return enlace

# Función para registrar la interacción de un suscriptor y almacenar su lada
def registrar_interaccion(user_id: int, phone_number: str) -> None:
    encrypted_phone_number = cipher_suite.encrypt(phone_number.encode()) if phone_number else b""
    lada = phone_number.split()[0] if phone_number else "Desconocida"
    suscriptores_activos[user_id] = {
        "ultima_interaccion": datetime.now(),
        "lada": lada,
        "phone_number": encrypted_phone_number
    }

# Comando de inicio que registra la interacción del usuario
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    keyboard = [[KeyboardButton("Compartir mi número de teléfono", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text('Por favor, comparte tu número de teléfono para continuar:', reply_markup=reply_markup)

# Manejador de mensajes de contacto
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    phone_number = update.message.contact.phone_number  # Obtener el número de teléfono del usuario
    registrar_interaccion(user_id, phone_number)
    await update.message.reply_text('¡Gracias por compartir tu número de teléfono!')

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
    if not musica_actual:
        respuesta = "No hay música compartida en las últimas 24 horas."
    await update.message.reply_text(respuesta)

# Comando para mostrar suscriptores activos en las últimas 24 horas y sus ladas
async def suscriptores(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    activos = [(user_id, info['lada'], cipher_suite.decrypt(info['phone_number']).decode() if info['phone_number'] else "No proporcionado") for user_id, info in suscriptores_activos.items()
               if datetime.now() - info['ultima_interaccion'] < timedelta(hours=24)]
    inactivos = [(user_id, info['lada'], cipher_suite.decrypt(info['phone_number']).decode() if info['phone_number'] else "No proporcionado") for user_id, info in suscriptores_activos.items()
                 if datetime.now() - info['ultima_interaccion'] >= timedelta(days=7)]
    respuesta = ""
    
    if activos:
        respuesta += "Suscriptores activos en las últimas 24 horas:\n"
        respuesta += "\n".join([f"ID: {user_id}, Lada: {lada}, Teléfono: {phone_number}" for user_id, lada, phone_number in activos])
    else:
        respuesta += "No hay suscriptores activos en las últimas 24 horas.\n"
    
    if inactivos:
        respuesta += "\nSuscriptores inactivos en los últimos 7 días:\n"
        respuesta += "\n".join([f"ID: {user_id}, Lada: {lada}, Teléfono: {phone_number}" for user_id, lada, phone_number in inactivos])
    else:
        respuesta += "No hay suscriptores inactivos en los últimos 7 días."
    
    await update.message.reply_text(respuesta)

def main() -> None:
    application = ApplicationBuilder().token("7250794654:AAF5vW_My4QEfmuTpp6YOYsC1RyrbhX205o").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, contact))
    application.add_handler(CommandHandler("musica", musica))
    application.add_handler(CommandHandler("mostrar_musica", mostrar_musica))
    application.add_handler(CommandHandler("suscriptores", suscriptores))

    application.run_polling()

if __name__ == "__main__":
    main()
