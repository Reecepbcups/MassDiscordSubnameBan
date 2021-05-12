#!/usr/bin/python
"""
# How to  Install
1 - Download Python 3.7 or 3.6   : https://www.python.org/downloads/
2 - Run this command  : python3 -m pip install discord.py
3 - Run this command  : python3 discord_ban_subnames.py 
                       (or py discord_ban_subnames.py)

4 - Invite bot to the servers you want to ban members subnames from.
5 - Run the `$bansubnames <subname>` command and wait for it to ban

# Why This Bot?
This bot is useful for servers which have been raided by acccounts
which start with the same name from raids. This software should only 
be used to clean up raids which prune can not do itself.

If you have any issues contact me on discord:
Reecepbcups#3370
"""

import time
import discord

# Discord token from Discord Developer Portal
TOKEN = "YOUR.TOKEN"      

# True - Outputs users names rather than banning
# False - Live mode, Will ban members
debug = True

# in seconds. From 0.1 -> 2.0
rate_limit_wait = 1.0

# ======= BOT START =======

# https://discordpy.readthedocs.io/en/latest/intents.html
intents = discord.Intents(messages=True, members=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in banfromname bot!')
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$logout_session'):
        '''
        Log out your client so you do not have to wait on the
        Websocket connection to die.
        Anyone can run this command, provided that happens just
        Remove this code section (from lines 45-52).
        '''
        await client.logout()


    if message.content.startswith('$bansubnames'):

        if len(message.content.split(" ")) < 2:
            await message.channel.send("Incorrect usage: $bansubnames <subname>")

        # The substring we want to match others to
        startsWithStr = message.content.split(" ")[1]

        # loop through all server members
        for member in client.get_all_members():

            # if players name starts with the input you provided above
            if member.display_name.startswith(startsWithStr):

                if(debug == True):
                    # Checking to make sure people are right, will show in terminal
                    print(f"Member {member.display_name} start with {startsWithStr}")
                else:

                    # ban players whose name starts with
                    time.sleep(rate_limit_wait)
                    print(f"Member {member.display_name} banned due to subname.")
                    await member.ban(reason="Banned for your name starting with {startsWithStr} (Discord Raid)", delete_message_days=7)

client.run(TOKEN)