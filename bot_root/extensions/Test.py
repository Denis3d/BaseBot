#
# Coded by DenisDd#6912
# Website : http://denis3d.ml
#

import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(Test(bot))


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
