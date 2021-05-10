#!/usr/bin/env python3
import discord
from Loader.bot_loader import STARTING_CHAR, bot

@bot.command(
	name="opiremangemoilepoiro",
	help=f"Just enter \"{STARTING_CHAR}opiremangemoilepoiro\".",
	brief=":JuL: o pire mange moi le poiro :JuL:"
)
async def opiremangemoilepoiro(ctx):
	await ctx.channel.send( file=discord.File("Resources/Miscellaneous/Poiro/poiro.png") )