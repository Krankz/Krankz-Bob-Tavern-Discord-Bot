# Import pathlib for working with files.
from pathlib import Path

# Path to Bob's quotes.
cwd = Path.cwd()
bob_path = Path.joinpath(cwd, 'bobq.txt')

def create_array(txt):
    # Open file 
    stream = open(bob_path)
    # Store quotes in an array
    result = stream.readlines()
    # Remove Whitespace.
    result = [s.strip("\n") for s in result]
    return result

BOB_QUOTES = create_array(bob_path)

def bob_printer(message):
    if int(message) in range(0,39):
        print(BOB_QUOTES[int(message)])
    else:
        print("Please enter a valid number! (0-38)")

bob_printer("38")