from discord.ext import commands

import json
import re


def create_default_config_file():
    with open('config.json', 'w+') as outfile:
        data = {}
        data['prefix'] = "!"
        data['version'] = "1.0.0"
        data['bot_base_version'] = "1.0.0"
        data['description'] = "Easy python discord bot using DenisDd#6912 work"
        data['presence'] = ["help {members_count} members"]
        data['presence_change_cooldown'] = 7

        json.dump(data, outfile, indent=4)


def format_message(s: str, bot: commands.Bot = None, ctx = None):
    if bot is not None:
        s = s.replace("{members_count}", str(len(bot.users)))

    return s

