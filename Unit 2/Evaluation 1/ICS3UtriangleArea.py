import math
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def heron_formula(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's Formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Round the area to 2 decimal places
    area = round(area, 2)
    
    return area
# Tells the user what the program does
print(f'{Fore.BLUE}This program will calculate and display the area of the triangle rounded to 2 decimal spots, that you enter the 3 lengths of.{Style.RESET_ALL}')

# Asks the user for each size of a side
a = input(f'{Fore.ORANGE}What size is the first side?{Style.RESET_ALL}')
b = input(f'{Fore.ORANGE}What size is the second side?{Style.RESET_ALL}')
c = input(f'{Fore.ORANGE}What size is the third side?{Style.RESET_ALL}')

# Gets the area of the triangle
area = heron_formula(a, b, c)

# Displays the area of the triangle
print(f'{Fore.GREEN}The area of that triangle is {area}')
