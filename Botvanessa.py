import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración básica de logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ================= CONFIGURACIÓN =================
TOKEN = "8879033068:AAHw3nGD-pMCXLfVoArTyXGr9w3wTtsDzf8"
ONLYFANS_URL = "https://goo.su/OM2bwY"
AUDIO_PATH = r"D:\Music\audio_2026-10-14_15-03-37.ogg"
PHOTO_PATH = r"C:\Users\Monsalves\OneDrive\Imágenes\Muro de OF\IMG_8892.JPG.jpeg"
STICKER_ID = "CAACAgIAAxkBA..."  # (Opcional)
# =================================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /start (se ejecuta automáticamente al entrar por enlace profundo)."""
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Capturar parámetros de deep linking si los hubiera
    args = context.args
    if args:
        logger.info(
            f"Usuario {user.id} entró con parámetro de enlace profundo: {args[0]}"
        )

    # 1. Enviar primero la foto configurada (para que aparezca arriba)
    try:
        with open(PHOTO_PATH, "rb") as photo_file:
            await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
    except Exception as e:
        logger.error(f"Error al enviar la foto: {e}")

    # 2. Enviar después el audio local de bienvenida (para que aparezca abajo)
    try:
        with open(AUDIO_PATH, "rb") as audio_file:
            await context.bot.send_audio(chat_id=chat_id, audio=audio_file)
    except Exception as e:
        logger.error(f"Error al enviar el audio local: {e}")

    # 3. Enviar el sticker (opcional)
    if STICKER_ID and not STICKER_ID.startswith("CAACAgIAAxkBA..."):
        try:
            await context.bot.send_sticker(chat_id=chat_id, sticker=STICKER_ID)
        except Exception as e:
            logger.error(f"Error al enviar el sticker: {e}")

    # 4. Configurar el botón inline con el corazón azul 💙
    keyboard = [[InlineKeyboardButton("🔥 Entrar a mi OnlyFans 💙", url=ONLYFANS_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 5. Texto personalizado y organizado
    mensaje = (
        "✨ **¡Hola de nuevo!** ✨\n\n"
        "🤭 Soy **Vanessa**. Qué alegría que estés por aquí.\n\n"
        "🔥 Te espero en mi lugarcito privado para que descubras "
        "lo mejor de mí y hablemos más de cerca. 👇"
    )

    # Enviar el mensaje con formato (Markdown) y el botón organizado
    await update.message.reply_text(
        mensaje, reply_markup=reply_markup, parse_mode="Markdown"
    )


def main() -> None:
    """Función principal para arrancar el bot de Vanessa."""
    application = Application.builder().token(TOKEN).build()

    # Registrar el manejador del comando start
    application.add_handler(CommandHandler("start", start))

    # Iniciar el bot en modo polling
    print("¡Bot Vanessa iniciado y listo para recibir usuarios!")
    application.run_polling()


if __name__ == "__main__":
    main()
