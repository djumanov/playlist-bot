import os
from telegram import (
    KeyboardButton, 
    Update, 
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram.ext import (
    Updater,
    Dispatcher,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters,
)
from db import PlaylistDatabase

TOKEN = os.environ['TOKEN']
db = PlaylistDatabase('db.json')


def start(update: Update, context: CallbackContext):
    """
    Start command
    """
    keyboard = [
        [KeyboardButton(text='Playlists'), KeyboardButton(text='Create Playlist')]
    ]
    user = update.message.chat
    if not db.add_user(user_id=user.id, username=user.username):
        update.message.reply_text("Eski do'stimiz safimizga qaytdi!", \
            reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))
        return 
    update.message.reply_text("Xush kelibsiz <b>Playlist Bot</b> ga!", \
        parse_mode='HTML', \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))


def view_playlists(update: Update, context: CallbackContext):
    """
    View playlists
    """
    user = update.message.chat
    keyboars = []
    for playlist in db.view_playlists(user.id):
        playlist_name = playlist['playlist_name']
        btn = InlineKeyboardButton(text=playlist_name, callback_data=f'{playlist_name}|{user.id}')
        keyboars.append([btn])
    if keyboars:
        update.message.reply_text("<b>Playlistlaringiz!</b>", parse_mode='HTML', \
            reply_markup=keyboars)
    else:
        update.message.reply_text("<b>Sizning playlistingiz yo'q ekan!</b>", parse_mode='HTML')


def select_playlist_name(update: Update, context: CallbackContext):
    """
    Add new playlist
    """
    user = update.message.chat
    db.update_status(user_id=user.id, status='create playlist')

    update.message.reply_text("<b>Iltimos playlist uchun nom tanlang!</b>", parse_mode='HTML')


def create_playlist(update: Update, context: CallbackContext):
    """
    Add new playlist
    """
    user = update.message.chat
    playlist_name = update.message.text
    db.add_playlist(playlist_name=playlist_name, user_id=user.id)
    db.update_status(user_id=user.id, status='regular')

    update.message.reply_text("<b>Playlist yaratildi!</b>", parse_mode='HTML')


def status_handler(update: Update, context: CallbackContext):
    user = update.message.chat
    status = db.get_status(user_id=user.id)
    if status == "create playlist":
        create_playlist(update=update, context=context)
    

def main() -> None:
    """Start the bot."""
    # updater 
    updater = Updater(token=TOKEN)

    # dispatcher
    dispatcher = updater.dispatcher
    # command handlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))

    # message handler
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Text(strings=['Playlists']), \
        callback=view_playlists))
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Text(strings=['Create Playlist']), \
        callback=select_playlist_name))

    # all message handler
    dispatcher.add_handler(handler=MessageHandler(filters=filters.ALL, callback=status_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()