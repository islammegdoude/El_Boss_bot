import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected !! ')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('-hi'):
        await message.channel.send('wa3alikom el hi')
    if message.content == 'hello':
        await message.channel.send('oskot ')
    if message.content == 'tiiiit':
        await message.channel.send('tiiiit nta thani')


@client.event
async def on_member_join(member):
    chatchannel = client.get_channel("your channel id ")
    await chatchannel.send(f'<@!{member.id}> mar7aban bika ya ibn tiiiiit')
    await member.send(f'<@!{member.id}> hello bik fi among us server m3ana ya tkon tiiiit ya tiiiit ')
    print(f'{member} has joined server !! ')
    roll = discord.utils.get(member.guild.roles, name='the boys')
    await member.add_roles(roll)


@client.event
async def on_member_remove(member):
    chatchanne = client.get_channel("your channel id ")
    await chatchanne.send(f'<@!{member.id}> krej weld tiiiit ')
    await member.send(f'<@!{member.id}> ya tiiiit  ')
    print(f'{member} has leave  server !! ')


@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('pong !!')


client.run('your bot id ')
