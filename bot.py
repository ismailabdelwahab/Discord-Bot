#!/usr/bin/env python3

# Bot related variables :
from Loader.bot_loader import STARTING_CHAR, bot
# Env File variables :
from Loader.env_loader import DISCORD_TOKEN, BOT_NAME

###### Importing Bot's commands #####
# Others:
import Commands.Dice.dice
import Commands.Hash.hash

# Language folder :
import Commands.Language.Translate.translate

# Miscellaneous folder :
import Commands.Miscellaneous.Ping.ping
import Commands.Miscellaneous.Sapin.sapin

#####################################

### TODO: HANDLE UNEXISTING COMMAND ????

###### Importing the on_message handler ######
import Message_event_handler.message_handler
##############################################

if __name__ == '__main__':
	print("[+] Starting bot.")
	bot.run( DISCORD_TOKEN )
	print("[+] End of bot.")