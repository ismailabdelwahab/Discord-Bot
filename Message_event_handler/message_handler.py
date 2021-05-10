#!/usr/bin/env python3
from Loader.bot_loader import bot
from Loader.env_loader import BOT_NAME

# Importing data related to human users on our server
from Loader.data_loader import human_users

@bot.event
async def on_message(msg):
	if msg.author == bot.user:
		return # Do not lister to msgs sent by the bot itself.
	if msg.content == f"{BOT_NAME} test":
		await msg.channel.send("> Test functionality is working. (uses the on_msg listener)")
	
	#################### REACTIONS ###########################
	for human in human_users:
		await react_to_names_in_msg( human["names"], human["user_id"], msg, human["emote"] )
	##########################################################

    # Allow the usage of commands while using this listener :
	await bot.process_commands(msg)


async def react_to_names_in_msg( names, user_id, msg, reaction):
	if user_id in msg.content:
		await msg.add_reaction(reaction); return
	for name in names:
		if name in msg.content.lower():
			await msg.add_reaction(reaction); return