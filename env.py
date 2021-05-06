#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# Load .env file :
load_dotenv()
# Retrieve env vars :
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
BOT_NAME = os.getenv('BOT_NAME')