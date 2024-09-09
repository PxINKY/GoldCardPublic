import discord
from random import random
from MaxEmbeds import EmbedBuilder
from discord.ext import commands
import os


class randomchampion(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Random Champion Cog Loaded!')

    # ----------------------
    # - Champion Name List -
    # ----------------------
    ChampionName = []
    with open('resources/RuleSets/ChampionNames.txt') as f:
        lines = f.readlines()
        ChampionName += lines
    # ----------------------
    # - Champion Quip List -
    # ----------------------
    ChampionQuip = []
    with open('resources/RuleSets/ChampionQuips.txt') as f:
        lines = f.readlines()
        ChampionQuip += lines

    arr = os.listdir("resources/Icons")
    ChampionFiles = []
    ChampionFiles += arr
    ChampionFiles.sort()

    @commands.command(aliases=['RC', 'randomchampion', 'RandomChampion'], help='Gives a random champion!')
    async def rc(self, ctx):
        min = 0
        max = len(self.ChampionName) - 1  # length of the list champion which is ever expanding
        ChampionNumber = int(random() * (max - min + 1) + min)

        Champion = EmbedBuilder(
            color=discord.Color.gold(),
            title=f'{self.ChampionName[ChampionNumber]}',
            description=self.ChampionQuip[ChampionNumber],
            thumbnail=f"attachment://{self.ChampionFiles[ChampionNumber]}",
            footer=[f'Requested by {ctx.author.name}']
        ).build()
        image = discord.File(f"resources/Icons/{self.ChampionFiles[ChampionNumber]}")
        await ctx.send(
            embed=Champion,
            file=image
        )


def setup(Bot):
    Bot.add_cog(randomchampion(Bot))
