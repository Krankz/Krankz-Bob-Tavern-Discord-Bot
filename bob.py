# Import pathlib for working with files.
from pathlib import Path

# Path to Bob's quotes.
cwd = Path.cwd()
bob_path = Path.joinpath(cwd, 'bobq.txt')

# Empty list to append quotes.
BOB_QUOTES = []

