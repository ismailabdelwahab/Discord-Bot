#!/usr/bin/env python3
from bot_loader import STARTING_CHAR, bot


CHRISTMAS_TREE_GIF = "https://tenor.com/view/fk-this-i-quit-nope-i-cant-christmas-tree-gif-14498008"

@bot.command(
	name="sapin",
	help=f"Just enter \"{STARTING_CHAR}sapin\" or\n\
	\"{STARTING_CHAR}sapin\" <Something> to throw a christmas tree at it.",
	brief="Let the bot throw a christmas tree in the chat."
)
async def sapin(ctx, *args):
	answer = f"> **{ctx.message.author.name}** is throwing a christams tree"
	if args == (): # No args given
		answer += "."
	else:
		answer += " at**"
		for arg in args:
			answer += f" {arg}"
		answer += "**."
	await ctx.channel.send( answer )
	await ctx.channel.send( CHRISTMAS_TREE_GIF )