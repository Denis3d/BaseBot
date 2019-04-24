#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#
__version__ = "1.0.0"

import discord
from discord.ext import commands

import os
import json

from bot import utils


def setup(bot):
    bot.add_cog(Server_info_channel(bot))


class Server_info_channel(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        if not os.path.isfile('./config/server_info_channel.json'):
            with open('./config/server_info_channel.json', 'w+') as outfile:
                data = {"guild_id": {"channel_id": {"name": "Member Count : {member_count}", "data_type": "members_count"}}}
                json.dump(data, outfile, indent=4)
        self.config = json.load(open('./config/server_info_channel.json', 'r'))

        print("server_info_channel %s extension loaded" % __version__)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        self.member(member)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        self.member(member)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        await self.channel()

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        await self.channel()

    async def channel(self, impacted_channel):
        for channel in self.config[str(impacted_channel.guild.id)]:
            data = 0
            if self.config[str(impacted_channel.guild.id)][channel]['data_type'] == "channel_count":
                data = len(channel.guild.channels)
            elif self.config[str(impacted_channel.guild.id)][channel]['data_type'] == "text_channel_count":
                data = len(impacted_channel.guild.text_channels)
            elif self.config[str(impacted_channel.guild.id)][channel]['data_type'] == "voice_channel_count":
                data = len(impacted_channel.guild.voice_channels)
            elif self.config[str(impacted_channel.guild.id)][channel]['data_type'] == "ccategories_count":
                data = len(impacted_channel.guild.categories)

            await impacted_channel.guild.get_channel(int(channel)).edit(
                name=self.config[str(impacted_channel.guild.id)][channel]['name'].replace("{data}", str(data)))

    async def member(self, member):
        for channel in self.config[str(member.guild.id)]:
            data = 0
            if self.config[str(member.guild.id)][channel]['data_type'] == "member_count":
                data = len(member.guild.members)
            elif self.config[str(member.guild.id)][channel]['data_type'] == "user_count":
                for m in member.guild.members:
                    if not m.bot:
                        data += 1
            elif self.config[str(member.guild.id)][channel]['data_type'] == "bot_count":
                for m in member.guild.members:
                    if m.bot:
                        data += 1

            await member.guild.get_channel(int(channel)).edit(
                name=self.config[str(member.guild.id)][channel]['name'].replace("{data}",
                                                                                str(data)))
