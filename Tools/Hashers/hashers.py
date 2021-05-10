#!/usr/bin/env python3

import hashlib


def HASH_WITH_ALGO( algo, to_hash ):
	""" Return the hash of "to_hash" using the "algo" as hash algorithm """
	return algo( to_hash.encode() ).hexdigest()


def HASH_MD5( to_hash ):
	return HASH_WITH_ALGO( hashlib.md5, to_hash )

def HASH_SHA1( to_hash ):
	return HASH_WITH_ALGO( hashlib.sha1, to_hash )

def HASH_SHA256( to_hash ):
	return HASH_WITH_ALGO( hashlib.sha256, to_hash )
