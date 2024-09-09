# Defines the coin flip process
def coin_flip():
    import random
    result = random.choice(['Heads', 'Tails'])
    return result

# Defines the loop that will stop the program after a specific # of heads has been flipped
def loop_until_heads(num_heads):
    heads = 0
    count = 0
    all_flips = []
    while heads < num_heads:
        result = coin_flip()
        if result == 'Heads':
            count += 1
            heads += 1
            all_flips.extend([result])
            print('HEADS!')
        elif result == 'Tails':
            count += 1
            all_flips.extend([result])
            print('TAILS!')
    return count

# Defines the main program
def main():
    # Prints a welcome message
    print("Welcome to Gary's Coin Flip Simulator!\n")
    # Asks the user for the number of heads they want to flip
    num_heads = int(input("How many heads would you like to flip? -"))
    # Calls the loop_until_heads function with the user's input
    count = loop_until_heads(num_heads)
    # Prints how many flips it took and all the sides it got
    print(f"It took {count} flips to get {num_heads} heads.")

# Runs the program
if __name__ == "__main__":
    main()
