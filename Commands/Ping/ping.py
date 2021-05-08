#!/usr/bin/env python3
from bot_loader import STARTING_CHAR, bot

@bot.command(
	name="ping",
	help=f"Just enter \"{STARTING_CHAR}ping\".",
	brief="Prints pong back to the channel, along with the bot's latency."
)
async def ping(ctx):
	await ctx.channel.send(f"> Pong! Lantency : {round(bot.latency*1000,2)} ms.")