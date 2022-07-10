import discord
import os

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_member_join(member):
  channel = client.get_channel(995474989132283964)
  message = await channel.send(f'Bem vindo ao lado certo {member.mention}'
  + ' <a:smiling_imp:995482100503416863>'
  + ' <a:money_mouth:995482642839502859>'
  + ' <a:hot_face:995482668521238562>')

@client.event
async def on_member_remove(member):
  channel = client.get_channel(995474989132283964)
  message = await channel.send(f'{member.mention} Saiu do servidor, vai tarde')
  

my_secret = os.environ['TOKEN']
client.run(my_secret)
