# imports the required modules
import math

# Defines the Variables
tax = 0.13

# Defines the tip process
def tip_process(subtotal: float):

    # Asks the user if they want to leave a tip
    tipping = input('Do you want to leave a tip?\n1: Yes\n2: No\n-')

    # Checks if they want to leave a tip or not
    if tipping == '1':
        # Asks the user if they want to tip a specific amount or by percentage
        tip_type = input('Do you want to tip a specific amount or by percentage?\n1: Specific amount\n2: Percentage\n-')
        # Checks which type of tip the user wants to leave
        if tip_type == '1':
            # Asks the user how much they want to tip
            raw_tip_amount = float(input('How much do you want to tip?\n- $'))
            tip_amount = round(raw_tip_amount, 2)
            return tip_amount
        elif tip_type == '2':
            # Asks the user what percentage they want to tip
            tip_percentage = float(input('What percentage do you want to tip?\n-'))
            # Calculates the tip amount based on the total bill and the tip percentage
            raw_tip_amount = (subtotal * tip_percentage) / 100
            tip_amount = round(raw_tip_amount, 2)
            return tip_amount
    elif tipping == '2':
        print('No tip will be left')
        tip_amount = 0
        return tip_amount

# Main program
def main():
    # Prints a welcome message
    print('Hello, welcome to Gary\'s tip calculator app!')
    # Asks the user for the subtotal of the bill
    subtotal = float(input('What is the subtotal of the bill?\n-$'))
    # Calculates the tax amount based on the subtotal and the tax rate
    tax_amount = round(subtotal * tax, 2)
    # Calculates the tip amount based on the subtotal and the tip process
    tip_amount = tip_process(subtotal)
    # Calculates the total bill amount based on the subtotal and the tax and tip
    total_bill = round(subtotal + tax_amount + tip_amount, 2)
    # Prints the subtotal and the tax owed and the tip and the final total
    print(f'----Your Receipt----\nSubtotal: {subtotal}\nTax: {tax_amount}\nTip: {tip_amount}\nTotal: {total_bill}\n--------------------')
    # Prints a thank you message
    print('Thank you for using Gary\'s tip calculator app!')

# Runs the main program
main()