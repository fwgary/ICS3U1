# Defines the print diamond function
def print_diamond(n):
    """
    Prints a diamond shape with n rows in the top half.
    """
    # Prints top half of the diamond
    for i in range(n):
        # Prints leading spaces
        for _ in range(n - i - 1):
            print(" ", end="")
        # Prints asterisks
        for _ in range(2 * i + 1):
            print("*", end="")
        print()

    # Prints bottom half of the diamond
    for i in range(n - 2, -1, -1):
        # Prints leading spaces
        for _ in range(n - i - 1):
            print(" ", end="")
        # Prints asterisks
        for _ in range(2 * i + 1):
            print("*", end="")
        print()

# Defines the main function
def main():
    # Gets the number of rows from the user
    n = int(input("Enter the number of rows in half the diamond: "))

    # Prints two diamonds side by side
    for i in range(2 * n - 1):
        # Prints first diamond
        print_diamond_row(n, i)
        # Prints a space between diamonds
        print(" ", end="")
        # Prints second diamond
        print_diamond_row(n, i)
        print()

def print_diamond_row(n, i):
    """
    Prints a single row of a diamond shape with n rows in the top half.
    """
    if i < n:
        # Prints leading spaces
        for _ in range(n - i - 1):
            print(" ", end="")
        # Prints asterisks
        for _ in range(2 * i + 1):
            print("*", end="")
    else:
        # Prints leading spaces
        for _ in range(i - n + 1):
            print(" ", end="")
        # Prints asterisks
        for _ in range(2 * (2 * n - i - 2) + 1):
            print("*", end="")

if __name__ == "__main__":
    main()