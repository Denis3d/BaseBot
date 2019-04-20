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
    bot.add_cog(Welcome_message(bot))


class Welcome_message(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        if not os.path.isfile('./config/welcome_message.json'):
            with open('./config/welcome_message.json', 'w+') as outfile:
                data = {'welcome_message': "Welcome to {member_name}", 'embed_color': {'r': 255, 'g': 0, 'b': 0}, 'welcome_message_channel': None}
                json.dump(data, outfile, indent=4)
        self.config = json.load(open('./config/welcome_message.json', 'r'))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(self.config['embed_color']['r'], self.config['embed_color']['g'],
                                           self.config['embed_color']['b']),
            description=utils.format_message(self.config['welcome_message'], bot=self.bot, member=member))
        member.guild.get_channel(self.config['welcome_message_channel']).send(embed=embed) if member.guild.get_channel(self.config['welcome_message_channel']) else print("Wrong channel id in config file")
