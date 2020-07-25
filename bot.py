import discord
import bob
from secret import token
from pathlib import Path

# Path to Bob's quotes.
cwd = Path.cwd()
bob_path = Path.joinpath(cwd, 'bobq.txt')

client = discord.Client()
BOB_QUOTES = bob.create_array(bob_path)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bob help'):
        await message.channel.send('Help!')
    elif message.content.startswith('$bob'):
        await message.channel.send('Exactly what were you looking for? (type $bob help)')

client.run(token)