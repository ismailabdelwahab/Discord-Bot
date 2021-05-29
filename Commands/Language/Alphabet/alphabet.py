#!/usr/bin/env python3
import discord
from Loader.bot_loader import bot
from Loader.emoji_loader import EMOJI_FORBIDEN

import json

def retrieve_alphabets():
	with open("Resources/Language/alphabets.json",'r') as f:
		alphabets = json.loads( f.read() )
	return alphabets

def get_available_lang_code( alphabets ):
	return [lang_code for lang_code in alphabets]

def proper_usage_alphabet( alphabets ):
	proper_usage = f"> {EMOJI_FORBIDEN} Wrong usage {EMOJI_FORBIDEN}.\n\
			 > Usage: $alphabet <Language code> (Available language code : "
	for lang_code in alphabets:
		proper_usage += f"{lang_code}, "
	return proper_usage[:-2]+")."

@bot.command(
	name="alphabet",
	help=f"Prints the alphabet of a language with prononciation and sounds examples.\n\
\tSupported languages: ar, ru, ko.",
	brief="Prints alphabet's letters, along with some elements to prononce them."
)
async def alphabet(ctx, *args):
	alphabets = retrieve_alphabets()
	available_lang_code = get_available_lang_code( alphabets )

	if( len(args) != 1 ):
		await ctx.channel.send("> Error : Wrong number of parameters.")
		await ctx.channel.send(proper_usage_alphabet(alphabets)); return
	lang_code = args[0].lower()
	if lang_code not in available_lang_code:
		await ctx.channel.send(proper_usage_alphabet(alphabets)); return

	selected_alphabet = alphabets[lang_code]
	alphabet_data = dump_alphabet_data_in_string( selected_alphabet )

	filename = put_in_file( lang_code, alphabet_data )

	await ctx.channel.send( file=discord.File(filename) )


def dump_alphabet_data_in_string( alphabet ):
	like_in_padding = 25
	string = f"{'Letter'} | {'Prononciation'} | {'Like in':^30} | {'Comment'}"
	for letter in alphabet:
		string += f"\n {letter:^5} | "
		string += f"{alphabet[letter]['prononciation']:^13} | "
		string += f"{alphabet[letter]['like-in']:^30}"
		if( alphabet[letter]['comment'] != ""):
			string += f" | {alphabet[letter]['comment']}"
	return string

def put_in_file( lang_code, text ):
	filename = f"/tmp/alphabet_{lang_code}.txt"
	with open( filename, "w") as f:
		f.write( text )
	print(f"\t[+]{{Alphabet}}File created: [ {filename} ]")
	return filename