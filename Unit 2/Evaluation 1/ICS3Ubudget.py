import random

def generate_budget():
    # Generate realistic random values for each budget item
    food = random.randint(300, 800)
    clothing = random.randint(100, 300)
    entertainment = random.randint(200, 500)
    rent = random.randint(800, 1500)

    # Gets the total budget
    total_budget = food + clothing + entertainment + rent

    # Gets the percentage of the total for each budget item
    food_percentage = round((food / total_budget) * 100)
    clothing_percentage = round((clothing / total_budget) * 100)
    entertainment_percentage = round((entertainment / total_budget) * 100)
    rent_percentage = 100 - (food_percentage + clothing_percentage + entertainment_percentage)

    # Print the budget items with their values and percentages
    print(f"Budget Item          Value ($)    Percentage (%)")
    print(f"-----------------------------------------------")
    print(f"Food                {food}         {food_percentage}%")
    print(f"Clothing            {clothing}         {clothing_percentage}%")
    print(f"Entertainment      {entertainment}         {entertainment_percentage}%")
    print(f"Rent                {rent}         {rent_percentage}%")
    print(f"-----------------------------------------------")
    print(f"Total Budget: ${total_budget}")

# Runs the program
generate_budget()