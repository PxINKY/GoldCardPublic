import discord
import os
from discord.ext import commands


class devcommands(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dev Cog Loaded!')

    # No longer needed, feel free to do what ever here
    # Hawk Tuah


def setup(Bot):
    Bot.load_extention(devcommands(Bot))
