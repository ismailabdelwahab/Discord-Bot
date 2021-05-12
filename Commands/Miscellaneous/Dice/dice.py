#!/usr/bin/env python3
from Loader.bot_loader import bot

from random import randint


############# Dice #########################
@bot.command(
	name="dice",
	help=f"Throw a 100 sided dice.",
	brief="Throw a 100 sided dice."
)
async def dice(ctx):
	number = randint(1, 100)
	answer = f"\
> {ctx.message.author.name} threw a 100 sided dice.\n\
> \tResult: **{number}** ."
	if number == 1:
		answer += "\n> (miskine you did 1.)"
	await ctx.channel.send(answer)
############################################