#!/usr/bin/env python3
from bot_loader import bot
from env import BOT_NAME

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return # Do not lister to messages sent by the bot itself.
	if message.content == f"{BOT_NAME} test":
		await message.channel.send("> Test functionality is working. (uses the on_message listener)")
		
    # Allow the usage of commands while using this listener :
	await bot.process_commands(message)