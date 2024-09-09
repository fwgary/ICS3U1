# Imports the required modules
import random

# Defines the generate function
def generate_pair():
    """Generate a pair of numbers between -5 and 5"""
    return random.randint(-5, 5), random.randint(-5, 5)

# Defines the main function
def main():
    all_numbers = []
    while True:
        num1, num2 = generate_pair()
        all_numbers.extend([num1, num2])
        
        # Sort the pair and display it along with the sum
        pair = sorted([num1, num2])
        print(f"Pair: {pair[0]}, {pair[1]} | Sum: {pair[0] + pair[1]}")
        
        # Check if the pair is the negative of each other
        if num1 == -num2:
            print(f"Program stopped because {num1} is the negative of {num2}")
            break
    
    # Display the sum of all generated numbers
    print(f"Sum of all numbers: {sum(all_numbers)}")

if __name__ == "__main__":
    main()