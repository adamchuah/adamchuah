import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot


@client.event 
async def on_ready( ):
	print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
   	if message.content == "jun" :
   		await client.send_message(message.channel, "Unblock me on Facebook")
   		await client.send_message(message.channel, ":heart_eyes:")

   	if message.content == "cookie" :
   		await client.send_message(message.channel, "Yum Yum")
   		await client.send_message(message.channel, ":heart_eyes:")

   	if message.content == "dick" :
   		await client.send_message(message.channel, "cibai no inv me to wedding")
   		await client.send_message(message.channel, ":sleeping:")


	# if message.content == "cookie" :
 #   		await client.send_message(message.channel, ":heart_eyes:")

   	
client.run("NDU4MjY2NDc4OTQxMzA2OTAw.DglNVg.F5OvaIOFL3C0_O3PFEUjASBTPQc") #Replace token with your bots token
