#!/usr/bin/env python3

# Bot related variables :
from bot_loader import STARTING_CHAR, bot
# Env File variables :
from env import DISCORD_TOKEN, BOT_NAME

###### Importing Bot's commands #####
import Commands.Ping.ping
import Commands.Dice.dice
#####################################

### TODO: HANDLE UNEXISTING COMMAND ????

###### Importing the on_message handler ######
import Message_event_handler.message_handler
##############################################

if __name__ == '__main__':
	print("[+] Starting bot.")
	bot.run( DISCORD_TOKEN )
	print("[+] End of bot.")