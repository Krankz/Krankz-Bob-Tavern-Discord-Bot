import discord
from discord.ext import commands
import bob
from pathlib import Path
import os 

token = os.environ(['TOKEN'])

def bob_lines():
    cwd = Path.cwd()
    bob_path = Path.joinpath(cwd, 'bobq.txt')
    result = bob.create_array(bob_path)
    return result

client = commands.Bot(command_prefix='$bob ')

BOB_QUOTES = bob_lines()

@client.event
async def on_ready():
        print(f"Created Array ({len(BOB_QUOTES)} lines)! Online!") 

@client.command()
async def docs(ctx):
    await ctx.send('https://github.com/Krankz/Krankz-Bob-Tavern-Discord-Bot')

@client.command()
async def say(ctx, *, number):
    await ctx.send(bob.bob_printer(number, BOB_QUOTES))

client.run(token)