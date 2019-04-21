#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#

import discord
from discord.ext import commands

import os
import json

from bot import utils


def setup(bot):
    bot.add_cog(Simple_command(bot))


class Simple_command(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        if not os.path.isfile('./config/simple_command.json'):
            with open('./config/simple_command.json', 'w+') as outfile:
                data = {"commands": {"command_name": {"command_content": "Hello", "command_color": {"r": 255, "g": 0, "b": 0}}}}
                json.dump(data, outfile, indent=4)
        self.config = json.load(open('./config/simple_command.json', 'r'))

        for command in self.config['commands']:
            self.bot.add_command(commands.Command(self.simple_command, name=command))

    async def simple_command(self, ctx: commands.Context):
        em = discord.Embed(description=self.config['commands'][ctx.command.name]['command_content'], colour=discord.Colour.from_rgb(self.config['commands'][ctx.command.name]['command_color']['r'], self.config['commands'][ctx.command.name]['command_color']['g'], self.config['commands'][ctx.command.name]['command_color']['b']))
        await ctx.send(embed=em)

