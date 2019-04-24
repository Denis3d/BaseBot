#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#
__version__ = '1.0.0'

import discord
from discord.ext import commands

import os
import json
import asyncio
import pkgutil
import sys

from bot import utils
import extensions

if not os.path.exists("./config/"):
    os.makedirs("./config/")
if not os.path.isfile('config.json'):
    utils.create_default_config_file()
config = json.load(open('config.json', 'r'))

if not os.path.isfile('config.json'):
    utils.create_default_config_file()
config = json.load(open('config.json', 'r'))
bot: commands.Bot = commands.Bot(description=config['description'], command_prefix=config['prefix'])
bot.config = config


def run(token: str):
    for importer, module, ispkg in pkgutil.iter_modules(extensions.__path__):
        print('Loading module %s' % module)
        bot.load_extension('extensions.' + module)
    if token is None:
        raise Exception("Please give a Token")
    bot.run(token)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print("+-----------------------------------+")
    print("|  Running as : " + str(bot.user.name))
    print("|  Version : " + config['version'])
    print("|  Discord.py version : " + discord.__version__)
    print("|  BaseBot : " + __version__)
    print("|  Bot ID:" + str(bot.user.id))
    print("+-----------------------------------+")
    bot.loop.create_task(update_presence())


async def update_presence():
    status = config['presence']
    if config['presence_change_cooldown'] is not 0:
        while True:
            for s in status:
                await bot.change_presence(activity=discord.Game(name=utils.format_message(s, bot=bot)))
                await asyncio.sleep(config['presence_change_cooldown'])
    else:
        await bot.change_presence(activity=discord.Game(name=utils.format_message(status[0], bot=bot)))

if __name__ == "__main__":
    if len(sys.argv) is 2:
        TOKEN = sys.argv[1]
    elif 'TOKEN' in os.environ:
        TOKEN = os.environ['TOKEN']
    else:
        TOKEN = None  # This will make the programm crash but create default config file of installed extensions

    run(TOKEN)
