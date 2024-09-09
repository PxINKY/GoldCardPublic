from random import random, shuffle
import discord
import os
from switchcase import switch
from discord.ext import commands
from MaxEmbeds import EmbedBuilder
import cassiopeia as cass


class pings(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping Cog Loaded!')



    @commands.command(help='Sends servers latency at a given time')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.Bot.latency * 1000)}ms')


    @commands.command(help='Enter a valid summoner name and region to get the summoner\'s profile', aliases=['cass', 's'])
    async def summoner(self, ctx, summonerName, region):
        summoner = cass.get_summoner(name=summonerName, region=(region.upper()))
        # send info in embed
        if summoner.exists:
            pfpurl = summoner.profile_icon.url
            embed = EmbedBuilder(
                title=f"{summoner.name}",
                description=f"Level: {summoner.level}",
                thumbnail=f"{pfpurl}",
                color=discord.Color.gold(),
                footer=[f"requested by {ctx.author.name}"]).build()
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sorry that summoner doesn't exist!")


def setup(Bot):
    Bot.add_cog(pings(Bot))
