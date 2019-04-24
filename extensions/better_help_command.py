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
    bot.add_cog(Better_help_command(bot))


class Better_help_command(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        if not os.path.isfile('./config/better_help_command.json'):
            with open('./config/better_help_command.json', 'w+') as outfile:
                data = {'enable_better_help_command': True}
                json.dump(data, outfile, indent=4)
        self.config = json.load(open('./config/better_help_command.json', 'r'))

        if self.config['enable_better_help_command']:
            self.bot.remove_command('help')
            self.bot.add_command(commands.Command(self.help_command, name="help"))
        print("Better_help_command %s extension loaded" % __version__)

    async def help_command(self, ctx: commands.Context, command_name: str = None):
        """Affiche ce message"""
        await self.bot.help_command.prepare_help_command(ctx, None)
        if command_name is not None:
            await self.usage(ctx, command_name)
        else:
            em = discord.Embed(colour=discord.Colour.blue(), description=self.bot.description)
            em.set_author(name="Aide de " + self.bot.user.name + ":", icon_url=self.bot.user.avatar_url)
            em.set_footer(text=self.bot.help_command.get_ending_note() + "\nBaseBot by DenisDd#6912 - http://denis3d.ml")
            for command in self.bot.commands:
                em.add_field(name=command, value=command.help if command.help is not None else "No description", inline=False)

            await ctx.send(embed=em)

    async def usage(self, ctx, command):
        """Affiche l'aide pour une commande spécifique et son utilisation"""

        request_command = self.bot.get_command(command)
        if request_command is None:
            raise commands.ArgumentParsingError
            return
        parent = self.bot.get_command(command).full_parent_name
        if len(self.bot.get_command(command).aliases) > 0:
            aliases = '|'.join(self.bot.get_command(command).aliases)
            fmt = '[%s|%s]' % (self.bot.get_command(command).name, aliases)
            if parent:
                fmt = parent + ' ' + fmt
            alias = fmt
        else:
            alias = self.bot.get_command(command).name if not parent else parent + ' ' + self.bot.get_command(
                command).name

        e = discord.Embed(colour=discord.Colour.blue())
        e.add_field(name='Usage : %s%s %s' % (self.bot.command_prefix,
            self.bot.get_command(command).name, self.bot.get_command(command).signature if self.bot.get_command(
                command).signature is not None else "No description"),
                    value=" - " + (
                        self.bot.get_command(command).help if self.bot.get_command(
                            command).help is not None else "No description") + "\n - Alias : " + alias)
        return await ctx.send(embed=e)
