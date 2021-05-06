#!/usr/bin/env python3

from bot_loader import STARTING_CHAR, bot

@bot.command(
	name="ping",
	help=f"Just enter \"{STARTING_CHAR}ping\". (This is the help message)",
	brief="Prints pong back to the channel. (This is the brief message)"
)
async def ping(ctx):
	await ctx.channel.send("pong (Done with the commands listener).")