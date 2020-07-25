# Import pathlib for working with files.
from pathlib import Path

# Path to Bob's quotes.
cwd = Path.cwd()
bob_path = Path.joinpath(cwd, 'bobq.txt')

# Open file 
stream = open(bob_path)

# Store quotes in an array
BOB_QUOTES = stream.readlines()
# Remove Whitespace.
BOB_QUOTES = [s.strip("\n") for s in BOB_QUOTES]
