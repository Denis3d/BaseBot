import discord
from discord.ext import commands

import os
import json
import asyncio

from . import utils

if not os.path.isfile('config.json'):
    utils.create_default_config_file()
config = json.load(open('config.json', 'r'))
bot: commands.Bot = commands.Bot(description=config['description'], command_prefix=config['prefix'])


def run(token: str):

    bot.run(token)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print(" +-----------------------------------+")
    print(" |  Running as : " + str(bot.user.name))
    print(" |  Version : " + config['version'])
    print(" |  Discord.py version : " + discord.__version__)
    print(" |  Discord.py version : " + config['bot_base_version'])
    print(" |  Bot ID:" + str(bot.user.id))
    print(" +-----------------------------------+")
    bot.loop.create_task(update_presence())


async def update_presence():
    status = config['presence']
    while True:
        for s in status:
            await bot.change_presence(activity=discord.Game(name=utils.format_message(s, bot=bot)))
            await asyncio.sleep(config['presence_change_cooldown'])
