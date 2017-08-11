import discord
import asyncio
from numpy import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

	if message.content.startswith('erp with me pimbot'):
		await client.send_message(message.channel, '*rubs your milky thighs*')
	if message.content.startswith('l-lewd'):
		await client.send_message(message.channel, "I'll show you lewd! *sticks finger up butte*")
	if message.content.startswith('bully me pimbot'):
		await client.send_message(message.channel, "I bet that would turn you on wouldn't it you fairy")
	if message.content.startswith('tell me about the jews pimbot'):
		await client.send_message(message.channel, '(((they))) are putting oestrogen in the water turning the frogs and our sons gay!')

    #if message.content.startswith('!best'):
       #myid = '<@201909896357216256>'
       #await client.send_message(message.channel, ' : %s is the best ' % myid)

	#if message.content.startswith('hello <@343915078074236929>'):
		#myid = '<@343915078074236929>'
		#await client.send_message(message.channel, myid + ' says hello')

	if message.content.startswith('<@343915078074236929>'):
		await client.send_message(message.channel, 'h-huh')
	if message.content.startswith('tfw no bf'):
		await client.send_message(message.channel, "I'll be your bf, i-if you want")
	if message.content.startswith('fuck you pimbot'):
		await client.send_message(message.channel, 'no u')
	if message.content.startswith('nini~'):
		await client.send_message(message.channel, 'goodnight qt')
	if message.content.startswith('no u'):
		await client.send_message(message.channel, 'no me')
	if message.content.startswith('bye bye pimbot'):
		await client.send_message(message.channel, 'bye bye~')
	if message.content.startswith('~github'):
		await client.send_message(message.channel, 'fork me or contribute to my development on github: \nhttps://github.com/Shiimoe/Pimbot')




	if message.content.startswith(message.content[0] + "-" + message.content[0]):
		await client.send_message(message.channel, 'Stop stuttering you gay cunt')

client.run('MzQzOTE1MDc4MDc0MjM2OTI5.DGlHtA.50snhJlQlLsEmm69zh-v8zcKs5Y')
