def create_array(txt):
    # Open file 
    stream = open(txt)
    # Store quotes in an array
    result = stream.readlines()
    # Remove Whitespace.
    result = [s.strip("\n") for s in result]
    return result



def bob_printer(message, quotes):
    if int(message) in range(0,39):
        print(quotes[int(message)])
    else:
        print("Please enter a valid number! (0-38)")

