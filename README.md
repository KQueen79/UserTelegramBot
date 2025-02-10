<div align="center">
  <img src="https://64.media.tumblr.com/52138e81f9b6378e43b2a6e0c8563874/cceeceecf04c75e3-fe/s96x96u_c1/2d838a79bc6b431a9cc8bf09866fcfdbc0e2ee9c.pnj" alt="Logo" width="150">
  <h1 style="color:#FFC918;">🎉 <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="40" height="40">
 Telegram Bot 🎉 <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="40" height="40">
 </h1>
  <p style="color:#333333;">
    Un bot de administración de Telegram que gestiona suscriptores y permite a los usuarios compartir la música que están escuchando, administra datos del usuario para su mejor control de modo organizado y de manera encriptada tanto la lada como la numeracion telefonica.
  </p>
</div>

---

## 🌟 Características Principales

- **🎧 Registro de Suscriptores Activos/Inactivos**: El bot registra la actividad de los suscriptores y los clasifica como activos o inactivos. Esta funcionalidad es fundamental para mantener un registro preciso de la participación en el canal.
- **🎶 Compartir Música**: Los usuarios pueden compartir las canciones que están escuchando. El bot genera automáticamente un enlace de descarga para que otros usuarios puedan escuchar la música compartida.
- **🔔 Notificaciones Automáticas**: Cada vez que un usuario comparte una nueva canción, el bot notifica automáticamente al canal, asegurando que todos los miembros estén al tanto de las últimas actualizaciones musicales.
- **⬇️ Enlace de Descarga**: Los usuarios pueden descargar las canciones compartidas directamente desde un enlace proporcionado por el bot.

## 📋 Comandos Disponibles

- **/start**: Inicia la conversación con el bot y solicita al usuario que comparta su número de teléfono.
- **/musica [nombre de la canción]**: Permite a los usuarios compartir el nombre de la canción que están escuchando y genera un enlace de descarga.
- **/mostrar_musica**: Muestra la música que los usuarios han compartido en las últimas 24 horas con enlaces de descarga.
- **/suscriptores**: Muestra una lista de suscriptores activos en las últimas 24 horas y suscriptores inactivos en los últimos 7 días, incluyendo su lada y número de teléfono.
- **/send**: Envía un mensaje al canal `@TU CANAL TELEGRAM`.
- **/recompensas**: Muestra cuántos puntos ha acumulado el usuario y las recompensas disponibles.
- **/encuesta**: Envía una encuesta interactiva para obtener feedback de los suscriptores.
- **/recordatorio [segundos]**: Establece un recordatorio para el tiempo especificado en segundos.

## 🛠️ Requisitos

- Python 3.8 o superior
- Biblioteca `python-telegram-bot`
- Biblioteca `cryptography`

## 🚀 Instalación

1. Clona este repositorio:

2. Instala las dependencias:

sh
pip install -r requirements.txt
Configura el archivo bot.py con tu token de bot de Telegram y la URL de tu servidor de archivos mp3.

📝 Uso
Ejecuta el bot:

sh
python bot.py
Abre Telegram y busca tu bot por su nombre.

Usa los comandos mencionados anteriormente para interactuar con el bot y gestionar el canal.

🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar en el proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz un commit (git commit -am 'Añadir nueva funcionalidad').

Sube tus cambios a la rama (git push origin feature/nueva-funcionalidad).

Abre un Pull Request.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
   ```sh
   git clone https://github.com/KQueen79/Telegram-Bot.git
   cd Telegram-Bot

