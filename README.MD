# Telegram Bot

Este es un bot de administración de Telegram diseñado para gestionar suscriptores y permitir a los usuarios compartir la música que están escuchando. El bot ofrece varias funcionalidades para mejorar la experiencia del usuario en un canal de Telegram.

## Características

- **Registro de Suscriptores Activos/Inactivos**: El bot registra la interacción de los suscriptores y clasifica a los usuarios como activos o inactivos.
- **Compartir Música**: Los usuarios pueden compartir la música que están escuchando y el bot genera un enlace para escuchar o descargar la canción.
- **Notificaciones Automáticas**: El bot notifica automáticamente al canal cuando un usuario comparte una nueva canción.
- **Enlace de Descarga**: Los usuarios pueden descargar las canciones compartidas directamente desde un enlace proporcionado por el bot.

## Comandos Disponibles
Lista de Comandos y Funciones:

/start

Descripción: Inicia la conversación con el bot y solicita al usuario que comparta su número de teléfono.

Función Asociada: start(update: Update, context: ContextTypes.DEFAULT_TYPE)

/musica [nombre de la canción]

Descripción: Permite a los usuarios compartir el nombre de la canción que están escuchando.

Función Asociada: musica(update: Update, context: ContextTypes.DEFAULT_TYPE)

Notificación: Notifica al canal @CMenvivo con el nombre de la canción que el usuario está escuchando.

/mostrar_musica

Descripción: Muestra una lista de la música que los usuarios han compartido en las últimas 24 horas.

Función Asociada: mostrar_musica(update: Update, context: ContextTypes.DEFAULT_TYPE)

/send

Descripción: Envía un mensaje al canal @TU CANAL.

Función Asociada: send_message_to_channel(update: Update, context: ContextTypes.DEFAULT_TYPE)

/suscriptores

Descripción: Muestra una lista de suscriptores activos en las últimas 24 horas y suscriptores inactivos en los últimos 7 días, incluyendo su lada y número de teléfono.

Función Asociada: suscriptores(update: Update, context: ContextTypes.DEFAULT_TYPE)

Funciones Adicionales:
registrar_interaccion(user_id: int, phone_number: str)

Descripción: Registra la interacción de un suscriptor y almacena su lada y número de teléfono encriptado.

Uso Interno: Llamada por la función contact para registrar los datos del usuario cuando comparte su número de teléfono.

contact(update: Update, context: ContextTypes.DEFAULT_TYPE)

Descripción: Maneja los mensajes de contacto cuando un usuario comparte su número de teléfono.

Uso Interno: Asociada al manejador de mensajes MessageHandler(filters.CONTACT, contact).



Generar Enlace de Descarga: La función generar_enlace_descarga crea un enlace para descargar la canción desde un servidor accesible.

Comando /musica: Almacena la canción que un usuario está escuchando y también genera un enlace de descarga para que los usuarios puedan descargar la canción directamente.

Comando /mostrar_musica: Muestra la música que los usuarios han compartido en las últimas 24 horas con un enlace de descarga.

Nota: Asegúrate de alojar los archivos mp3 en un servidor accesible y de actualizar la variable base_url con la URL de tu servidor.





## Requisitos

- Python 3.8 o superior
- Biblioteca `python-telegram-bot`
- Biblioteca `cryptography`

## Instalación

1. Clona este repositorio:
   ```plaintext
   git clone https://github.com/KQueen79/Telegram-Bot.git
   cd Telegram-Bot


by @KQueen79
