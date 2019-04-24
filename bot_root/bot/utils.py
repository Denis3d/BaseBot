#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#

import discord
from discord.ext import commands

import json
import re


def create_default_config_file():
    with open('config.json', 'w+') as outfile:
        data = {'prefix': "!", 'version': "1.0.0", 'description': "Easy python discord bot using DenisDd#6912 work",
                'presence': ["help {members_count} members"], 'presence_change_cooldown': 7}
        json.dump(data, outfile, indent=4)


def format_message(s: str, bot: commands.Bot = None, ctx = None, member: discord.Member = None):
    if bot is not None:
        s = s.replace("{members_count}", str(len(bot.users)))

    if member is not None:
        s = s.replace("{member_name}", member.display_name)
        s = s.replace("{member_id}", str(member.id))
        s = s.replace("{guild_name}", member.guild.name)
        s = s.replace("{guild_id}", str(member.guild.id))
    return s

