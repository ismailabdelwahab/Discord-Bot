#!/usr/bin/env python3
from Loader.bot_loader import bot
from Loader.emoji_loader import EMOJI_FORBIDEN

from Tools.Hashers.hashers import HASH_MD5, HASH_SHA1, HASH_SHA256


def proper_usage_hash():
	proper_usage = f"> {EMOJI_FORBIDEN} Wrong usage {EMOJI_FORBIDEN}.\n\
			 > Usage: $hash <**Hash algorithm**> <**Stuff to hash**>\n\
			 > Supported hash algorithms:"
	for algo in list(SUPPORTED_HASH_ALGO.keys()):
		proper_usage += f" {algo}"
	return proper_usage + "."

SUPPORTED_HASH_ALGO ={
	"md5": HASH_MD5,
	"sha1": HASH_SHA1,
	"sha256": HASH_SHA256
}

@bot.command(
	name="hash",
	help=f"Used to hash a string using you algorithm of choice.\n\
	Supported algorithms : MD5, SHA1, SHA256.",
	brief="Hash your string and prints the output."
)
async def hash(ctx, *args):
	if len(args) < 2 or args[0].lower() not in list(SUPPORTED_HASH_ALGO.keys()):
		await ctx.channel.send( proper_usage_hash()); return

	algorithm_name = args[0].lower()
	algorithm_to_use = SUPPORTED_HASH_ALGO[ algorithm_name]
	string_to_hash = " ".join( word for word in args[1:])
	
	hash_calculated =  algorithm_to_use( string_to_hash )

	await ctx.channel.send( 
		f"> [**{algorithm_name}**] of string [\"**{string_to_hash}**\"]\n\
		> Value: [ **{hash_calculated}** ] ." 
	)