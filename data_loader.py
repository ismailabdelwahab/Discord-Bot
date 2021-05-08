#!/usr/bin/env python3

import json

############# HUMAN USERS ######################
with open("Resources/humans.json",'r') as f:
	humans = json.load(f)

human_users = []
for human_key in humans:
	human_users.append( humans[human_key] )

ADRIEN = humans["ADRIEN"]
AHMED = humans["AHMED"]
AMINE = humans["AMINE"]
ISMAIL = humans["ISMAIL"]
KHALED = humans["KHALED"]
SALIM = humans["SALIM"]
TANGUY = humans["TANGUY"]
################################################