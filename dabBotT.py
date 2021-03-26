#Input "python -m pip install -U discord.py" into cmd
#If the libraries/modules don't exist.
import random #for any rng
import discord #for socketing with discord
import shelve
import ast
import re
from discord.ext.commands import Bot
from discord.ext import commands
#from PyNaCl import *


client = discord.Client()
bot_prefix= "!d "
description = '''A meme Bot'''
client = commands.Bot(command_prefix=bot_prefix,description=description)


#There should be a client.run() somewhere in this file, but i deleted it, because i don't want people hijacking my bot 8-)





FortyBotCount =0
MsgCount = 0
lastmsg =""	

voiceChat = 0
	






@client.event
async def on_ready():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("Dab on the memers")
	print("Dabbing on haters since	", client.user.name,client.user.id," Written by a lazy CS student")

	
@client.command(pass_context=True, description="""pong! I will respond if I am awake.""")
async def ping(ctx):
	"""Respond if I'm awake"""
	await client.say("<:BigSneeze:483804899679928320>") #this is a code for a dab emote on the server this bot runs on.
	

	

def random_msg(): #return a random message from the list defined inside.
	msgs = ["<:thehoff:492456495666167828>","<:illallowit:609923168072630272>","Dude nice","<:thonk:580631128981897216>","<:OrangeYouGlad:504718303000788992>","<:JEB:548288566397108225>","dope'","hehe","haha tru","Same tbh","basically"]
	reply = msgs[random.randrange(len(msgs))]
	
	return reply
	
def hi_reply(): # messages to reply with if the Bot is mentioned directly
	msgs = ["Massive Meme energy, Amirite?","Same","Meme","You Water Drinker","I'll allow it","dork","shut up","shut the up","hush","moo", "haha funni", "dank","(something funny)","hecc", "o dang", "hecks"]
	reply = msgs[random.randrange(len(msgs))]
	
	return reply


def linux_reply(): #There's a person on the server this bot runs on that won't shut up about Linux, this function is used to annoy him specifically
	msgs = ["Fortybot uses Linux","Fortybot uses Arch btw","sudo make me a sandwich","vim stands for 'very increasingly moronic'","rm -rf /","anyone want to play SuperTuxKart?","Mint is the best Distro","wine is not Gatorade","<:linux:422976286533615616>","<:linuxer:422980269893746688>", "mkdir funny_memes", "gcc -o dabBot dabBot.c","Segmentation Fault","This incident will be reported.", "tbh", "Just so everyone knows, this bot was written in MS word"]
	reply = msgs[random.randrange(len(msgs))]
	
	return reply

def global_msg(): #Bot will send a random msg to server after a few messages form real users
	msgs = ["Vermin Supreme 2020","Dang", "Sure", "I mean, sure", "It can be interpereted that way, yes", "Yes, but actually no","Imma interject here just to call you out, you wrong doofus", "I can't believe it's not butter","which serves as a metacomentary on the human experience","is that true or nah?","you're not wrong","annoying bots, amirite?","let's be real here tho, that's not gonna happen","same","man, if i had a dollar for every brain you didn't have, i'd have 20 dollars","no u","<:BigSneeze:483804899679928320>","k", "tbh","||hah gottem||"]
	reply = msgs[random.randrange(len(msgs))]
	
	return reply
	
	
	
def a_joke(): #some really bad jokes that can be summoned on command
	jokes = ["I attended a funeral for a recent family member. I asked his widdowed wife if I could say a word on his behalf and she agreed. 'Plethora' I said. 'Thanks' the wife said, teary-eyed, 'that means a lot'" ,"Ever wonder why you don't see elephants hiding in trees? Turns out they're really good at it" ,"What's the difference between a Piano and a Tuna? You can't Tune a fish","A teacher once found a student's work covered in cheese. She had no choice but to grate it","Bannt's Standup Career", "A tall man walks into a bar... Ouch!","Orange you glad i didn't say bananna?","What do you call a deaf musician? Anything you want, he can't hear you lmao","I really hate Russian Dolls... they're so full of themselves","dabBot is a quality bot"]
	reply = jokes[random.randrange(len(jokes))]
	return reply

def any_msg(): #to make things more interesting, randomly select from above message lists
	reply = ""
	choice = random.randrange(0,5)
	
	if choice == 1:
		reply = hi_reply()
	elif choice ==2:
		reply = linux_reply()
	elif choice == 3:
		reply = random_msg()
	else:
		reply = global_msg()
		

	return reply


def t(): #test fucntion, similar to ping()
	return "<:mascot:538450020156833793>"

	
		
	
'''
@client.command(pass_context=True)	
async def kys(ctx):
	client.close()
	'''

	
def random_game(): #Bot will select a random game to be seen playing in the UI
	msgs = ["Prison Architect", "Dota Underlords","Untitled Goose Game","the coustom CAH deck", "Castle Risk", "on Linux","Orbital Tilt","a game","Buddyfight","MTG","Team Fortress 2","the Saxophone","with derfinshna's cat","with InfernalMushroom","Nethack","RobloX","Haha funny Game 2019","on a bash shell","on cmd","an video game"]
	reply = msgs[random.randrange(len(msgs))]
	
	return reply
	

@client.event	
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	global FortyBotCount,lastmsg,MsgCount
	channel= message.channel
	
	
	#print(lastmsg)
	if("{0.author.name}".format(message) == "test" ):#and random.randrange(0,6) == 1
		#print(FortyBotCount)
		if(FortyBotCount >=2):
			
		#emoji = discord.emoji(name="s")
			if(re.search(r"im.*",message.content) or "I'm" in message.content or "Im" in message.content or "i'm" in message.content):
				#await message.author.add_roles(discord.utils.get(message.author.guild.roles,name="Castle Risk Enthusiast"))
				return
		else:
			if(re.search(r"im .*",message.content) or "I'm" in message.content or "Im" in message.content or "i'm" in message.content):
				FortyBotCount = FortyBotCount +1
		#await channel.send(u"\U0001F1F8" )
		#await message.add_reaction(u"\U0001F1E6" )
		#await message.add_reaction(	u"\U0001F1F1" )
		#await message.add_reaction(u"\U0001F1F9" )
		#await message.add_reaction(u"\U0001F1FE" )

	if "I'm Dad!" in message.content:
		await message.add_reaction(u"\U0001F5D1" )
	
	keyWords = ["dab","dabbot","yeet","win","!d"]	
	if(random.randrange(2) <2):
		
		await client.change_presence(activity=discord.Game(name=random_game()))
		
		
	#message.content.startswith("")
	#message.content
#await channel.send(msg)	
		
	
	if("dab" in message.content or "Dab" in message.content):
		#await channel.send(random_msg())
		await channel.send("<:BigSneeze:483804899679928320>")
		
	if("buddyfight" in message.content or "Buddyfight" in message.content):
		await channel.send("Hype")
	
			
	
	#if "{0.author.name}".format(message) == "FortyBot" and FortyBotCount >=5:
		#if(random.randrange(0,4) == 2):
		#	await channel.send( linux_reply())
		#FortyBotCount = 0
	#elif "{0.author.name}".format(message) == "FortyBot" and FortyBotCount <5:
	#	FortyBotCount = FortyBotCount +1
		
	if MsgCount >=6 and FortyBotCount <5:
		if(random.randrange(0,6)==2):
			await channel.send(any_msg())
		MsgCount = 0	
	elif MsgCount <15:
		MsgCount = MsgCount +1
	#else:
	#	await channel.send("yo <@102171989896105984> Am i annoying yet?")
	
	if(message.content == lastmsg and message.content not in keyWords):
		##msg = lastmsg 
		##l
		try:
			await channel.send(lastmsg)
		except:
			#await channel.send("same")
			lastmsg = ""
	else:
		
		lastmsg = message.content
		
		
	if("!d" in message.content):
		if("come chat" in message.content):
			#voiceChat = message.author.voice.channel
			voiceChat = await message.author.voice.channel.connect()
			
			
		if("gtfo" in message.content):
			try:
				await message.author.voice.channel.connect()
			except:
				pass
			await client.voice_clients[0].disconnect()
			#voiceChat.disconnect()
			#await message.author.voice.channel.disconnect()
		if("tell a joke" in message.content):
			await channel.send(a_joke())
			
	
		lastmsg = ""
		
	await client.process_commands(message)
	
	
	
		
		#print()
	
 


	


#s.ping