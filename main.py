import logging
from os import environ

from telethon import events
from telethon.sync import TelegramClient

from commands import redes_sociales
from phrases_db import BotDb

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = TelegramClient('bot', int(environ['API_ID']), environ['API_HASH']).start(bot_token=environ['BOT_TOKEN'])
bot_db = BotDb()


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):

    await event.respond(f'Hola { (await event.get_sender()).first_name }, ¿En qué puedo ayudarte?')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/comunidad'))
async def community(event):
    await event.respond('\n'.join([f'{item[0]}: {item[1]}' for item in redes_sociales.items()]))


@bot.on(events.NewMessage(pattern='/inspirame'))
async def community(event):
    phrase, author = bot_db.get_phrase()
    await event.respond(f'**{phrase}**\n- __{author}__')


@bot.on(events.NewMessage())
async def new_message(event):
    print(event.sender.first_name)


@bot.on(events.ChatAction())
async def handler(event):
    if event.user_joined:
        print(event)
        await event.reply(f'Bienvenid🤖 !!')


def main():
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()
