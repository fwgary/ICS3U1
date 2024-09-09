# Defines the function to check the angles
def checks_the_angles(angle1, angle2, angle3):
    # Check if the angles add up to 180
    if angle1 + angle2 + angle3 != 180:
       type = "Not a Triangle"
       return type
    elif angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        type = "Not a Triangle"
        return type
    elif angle1 == angle2 == angle3:
        type = "Equilateral"
        return type
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        type = "Isosceles"
        return type
    else:
        type = "Scalene"
        return type

# Defines the main function
def main():
    # Asks the user for the three angles
    angle1 = float(input("Enter the first angle (in degrees): "))
    angle2 = float(input("Enter the second angle (in degrees): "))
    angle3 = float(input("Enter the third angle (in degrees): "))
    # Runs the function to check the angles
    type = checks_the_angles(angle1, angle2, angle3)
    # Prints the result
    print("The type of the triangle is: ", type)

# Runs the main program
if __name__ == "__main__":
    main()
