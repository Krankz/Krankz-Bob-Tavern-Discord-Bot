import discord
from discord.ext import commands
import bob
from secret import token
from pathlib import Path

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
async def say(ctx, *, number):
    await ctx.send(bob.bob_printer(number, BOB_QUOTES))

client.run(token)