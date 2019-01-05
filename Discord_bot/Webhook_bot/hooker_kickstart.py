import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot


@client.event 
async def on_ready( ):
	print("Hooker Bot Status: Online ") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
   	if message.content == "jun" :
   		await client.send_message(message.channel, "Unblock me on Facebook")
   		await client.send_message(message.channel, ":heart_eyes:")

   	if message.content == "cookie" :
   		await client.send_message(message.channel, "Unblock me on Facebook")
   		await client.send_message(message.channel, ":heart_eyes:")

	# if message.content == "cookie" :
 #   		await client.send_message(message.channel, ":heart_eyes:")

   	
client.run("NDU4MzAyODYzMjc4NjA0MzE4.Dglreg.Yf12LjAgZl9a9fS0KWjNj_70G-A") #Replace token with your bots token
