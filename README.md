# Playlist Telegram Bot
This Telegram bot allows users to create and manage their own playlists. Users can add new items to their playlists, as well as view, edit, and delete existing items.

## Usage
To use the bot, simply search for the bot on Telegram and start a conversation with it. From there, you can use the following commands to interact with the bot:

- `/add [item name] [item details]` - Add a new item to your playlist
- `/view` - View your current playlist
- `/edit [item number] [new item name] [new item details]` - Edit an existing item in your - playlist
- `/delete [item number]` - Delete an item from your playlist

## Requirements
This bot requires a Telegram bot token to function. This can be obtained by creating a new bot on Telegram and obtaining the API key.

## Project Structure
A project structure defines the organization of the different components and files of a project, such as the source code, test files, documentation, and configuration files.

Here is an example of a basic project structure for a Telegram playlist bot using TinyDB:

```
telegram_playlist_bot/
    |- bot.py
    |- db.py
    |- user.py
    |- README.md
    |- requirements.txt
    |- playlist.json
    |- tests/
        |- test_bot.py
        |- test_db.py
        |- test_user.py
```

`bot.py`: This file contains the code for the Telegram bot, including the functions for handling commands and interacting with the user. \
`db.py`: This file contains the code for the TinyDB database, including the functions for connecting to the database, creating tables, inserting data, querying data, and updating/deleting data. \
`user.py`: This file contains the code for the user class, including the functions for adding, viewing, editing, and deleting items from the playlist. \
`README.md`: This file provides an overview of the project, including information on how to install and use the bot. \
`requirements.txt`: This file lists the required dependencies for the project.
playlist.json: This file contains the playlist data stored using TinyDB in json format. \
`tests/`: This directory contains test files for the bot, database, and user classes.
You can also use more complex project structures, like including a config folder, assets folder, docs folder based on your project's requirements.
