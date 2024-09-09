# Defines the fine rates
'''
1 to 20 km/h over the limit = $100 Fine
21 to 30 km/h over the limit = $250 Fine
31 to more km/h over the limit = $500 Fine
'''

# Defines the function to check the speed difference between the drivers speed and the speed limit
def check_diff(speed_limit, speed):
    speed_diff = speed - speed_limit
    return speed_diff

# Defines the function to check if the drivers speed was over the speed limit
def check_speed(speed_diff):
    # Checks the speed difference and returns the fine rate
    if speed_diff <= 20 and speed_diff >= 1:
        fine = 100
        return fine, speed_diff
    elif speed_diff <= 30 and speed_diff >= 21:
        fine = 250
        return fine, speed_diff
    elif speed_diff >= 31:
        fine = 500
        return fine, speed_diff  # Return speed_diff here

# Defines the main function
def main():
    # Prints a welcome message
    print("Welcome to Gary's Speed Fine Calculator!\n")
    # Asks the user for the speed limit
    speed_limit = float(input("Please enter the speed limit: "))
    # Asks the user for the drivers speed
    speed = float(input("Please enter the driver's speed: "))
    # Checks the speed difference and fine rate
    speed_diff = check_diff(speed_limit, speed)
    if speed_diff <= 0:
        print("The driver's speed was within the speed limit.\nSo they dont get a fine.")
    else:
        fine, speed_diff = check_speed(speed_diff)
        print(f"The speed limit was {speed_limit}:\nThe driver was going {speed}:\nWhich is {speed_diff} over the speed limit:\nSo their fine is ${fine}:")

# Runs the main program
if __name__ == "__main__":
    main()