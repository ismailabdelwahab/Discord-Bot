#!/usr/bin/env python3

# Bot related variables :
from Loader.bot_loader import STARTING_CHAR, bot
# Env File variables :
from Loader.env_loader import DISCORD_TOKEN, BOT_NAME

###### Importing Bot's commands #####

# Language folder :
import Commands.Language.Translate.translate
import Commands.Language.Alphabet.alphabet

# Miscellaneous folder :
import Commands.Miscellaneous.Dice.dice
import Commands.Miscellaneous.Hash.hash
import Commands.Miscellaneous.Ping.ping
import Commands.Miscellaneous.Sapin.sapin
import Commands.Miscellaneous.Poiro.opiremangemoilepoiro

#####################################

### TODO: HANDLE UNEXISTING COMMAND ????

###### Importing the on_message handler ######
import Message_event_handler.message_handler
##############################################

if __name__ == '__main__':
	print("[+] Starting bot.")
	bot.run( DISCORD_TOKEN )
	print("[+] End of bot.")