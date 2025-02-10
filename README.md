# UserTelegramBot
Bot para administrar Usuarios, tener un control de sus numeros de telefono registro, mensajes automaticos, entre otras funciones por ejemplo el compartir que es lo que el usuario esta escuchando con opción a descargar el audio.
<div align="center">
  <img src="https://user-images.githubusercontent.com/your-logo.png" alt="Logo" width="200">
  <h1 style="color:#FFC918;">🎉 Telegram Bot 🎉</h1>
  <p style="color:#333333;">
    Un bot de administración de Telegram que gestiona suscriptores y permite a los usuarios compartir la música que están escuchando. ¡Vamos a rockear! 🎸
  </p>
</div>

---

## 🌟 Características

- **🎧 Registro de Suscriptores Activos/Inactivos**: El bot registra la interacción de los suscriptores y clasifica a los usuarios como activos o inactivos.
- **🎶 Compartir Música**: Los usuarios pueden compartir la música que están escuchando y el bot genera un enlace para escuchar o descargar la canción.
- **🔔 Notificaciones Automáticas**: El bot notifica automáticamente al canal cuando un usuario comparte una nueva canción.
- **⬇️ Enlace de Descarga**: Los usuarios pueden descargar las canciones compartidas directamente desde un enlace proporcionado por el bot.

## 📋 Comandos Disponibles

- `/start`: Inicia la conversación con el bot y solicita al usuario que comparta su número de teléfono.
- `/musica [nombre de la canción]`: Permite a los usuarios compartir el nombre de la canción que están escuchando y genera un enlace de descarga.
- `/mostrar_musica`: Muestra la música que los usuarios han compartido en las últimas 24 horas con enlaces de descarga.
- `/suscriptores`: Muestra una lista de suscriptores activos en las últimas 24 horas y suscriptores inactivos en los últimos 7 días, incluyendo su lada y número de teléfono.
- `/send`: Envía un mensaje al canal `@CMenvivo`.
- `/recompensas`: Muestra cuántos puntos ha acumulado el usuario y las recompensas disponibles.
- `/encuesta`: Envía una encuesta interactiva para obtener feedback de los suscriptores.
- `/recordatorio [segundos]`: Establece un recordatorio para el tiempo especificado en segundos.

## 🛠️ Requisitos

- Python 3.8 o superior
- Biblioteca `python-telegram-bot`
- Biblioteca `cryptography`

## 🚀 Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu_usuario/Telegram-Bot.git
   cd Telegram-Bot
