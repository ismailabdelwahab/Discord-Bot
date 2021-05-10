#!/usr/bin/env python3
from bot_loader import bot
from emoji_loader import EMOJI_FORBIDEN

import requests
import json

def proper_usage_translate():
	return f"> {EMOJI_FORBIDEN} Wrong usage {EMOJI_FORBIDEN}.\n\
			 > Usage: $translate <Stuff to translate>"

TRANSLATE_API_URL = "https://libretranslate.com/translate"
LANGUAGES = {
	"fr":":flag_fr:",
	"en":":flag_gb:",
	"ar":":flag_eg:",
	"ru":":flag_ru:",
	"ko":":flag_kr:"
}

@bot.command(
	name="translate",
	help=f"Used to translate French words (or sentences) to multiple languages.\n\
\tSupported languages: fr, en, ar, ru, kr.",
	brief="Translate French words/sentences to English(en), Arabic(ar), Russian(ru), Korean(ko)."
)
async def translate(ctx, *args):
	if args == ():
		await ctx.channel.send( proper_usage_translate() ); return

	to_tranlate = " ".join(arg for arg in args)
	source_code = "fr"
	print(f"Translating from [French] : [{to_tranlate}]")
	
	answer = f"Translating [**{to_tranlate}**] from French {LANGUAGES[source_code]}:\n"
	for target_code in LANGUAGES:
		if target_code == source_code:
			continue # Do not translate in the same language
		translated =  translate_source_target( source_code, target_code, to_tranlate)
		answer += f"> {LANGUAGES[target_code]} **{target_code.upper():^4}**\t|\t{translated:^20}\n"

	await ctx.channel.send( answer )

def translate_source_target( source_code, target_code, to_tranlate ):
	""" Return the translation of "to_translate" in Unicode format.

	Make a request to translate "to_translate" from language code "source_code" 
	to the target language of code "target_code".
	Uses libretranslate API.
	"""
	body = {"q":to_tranlate,"source":source_code,"target":target_code}
	response = requests.post( TRANSLATE_API_URL, data=body )

	json_answer = json.loads( response.text )
	translated = json_answer["translatedText"]
	print( "\t" + translated)
	return u"{0}".format(translated)