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

Características Principales:
Registro de Suscriptores Activos/Inactivos: El bot registra la actividad de los suscriptores y los clasifica como activos o inactivos. Esta funcionalidad es fundamental para mantener un registro preciso de la participación en el canal.

Compartir Música: Los usuarios pueden compartir las canciones que están escuchando. El bot genera automáticamente un enlace de descarga para que otros usuarios puedan escuchar la música compartida.

Notificaciones Automáticas: Cada vez que un usuario comparte una nueva canción, el bot notifica automáticamente al canal, asegurando que todos los miembros estén al tanto de las últimas actualizaciones musicales.

Enlace de Descarga: Los usuarios pueden descargar las canciones compartidas directamente desde un enlace proporcionado por el bot.

Comandos Disponibles:
/start: Inicia la conversación con el bot y solicita al usuario que comparta su número de teléfono.

/musica [nombre de la canción]: Permite a los usuarios compartir el nombre de la canción que están escuchando y genera un enlace de descarga.

/mostrar_musica: Muestra la música que los usuarios han compartido en las últimas 24 horas con enlaces de descarga.

/suscriptores: Muestra una lista de suscriptores activos en las últimas 24 horas y suscriptores inactivos en los últimos 7 días, incluyendo su lada y número de teléfono.

/send: Envía un mensaje al canal @CMenvivo.

/recompensas: Muestra cuántos puntos ha acumulado el usuario y las recompensas disponibles.

/encuesta: Envía una encuesta interactiva para obtener feedback de los suscriptores.

/recordatorio [segundos]: Establece un recordatorio para el tiempo especificado en segundos.

Requisitos:
Python 3.8 o superior

Biblioteca python-telegram-bot

Biblioteca cryptography

Instalación:
Clona este repositorio:

sh
git clone https://github.com/tu_usuario/Telegram-Bot.git
cd Telegram-Bot
Instala las dependencias:

sh
pip install -r requirements.txt
Configura el archivo bot.py con tu token de bot de Telegram y la URL de tu servidor de archivos mp3.

Uso:
Ejecuta el bot:

sh
python bot.py
Abre Telegram y busca tu bot por su nombre.

Usa los comandos mencionados anteriormente para interactuar con el bot y gestionar el canal.

Contribuciones:
Las contribuciones son bienvenidas. Si deseas colaborar en el proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz un commit (git commit -am 'Añadir nueva funcionalidad').

Sube tus cambios a la rama (git push origin feature/nueva-funcionalidad).

Abre un Pull Request.

Licencia:
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Gracias por usar nuestro bot de Telegram! Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un issue en el repositorio.
