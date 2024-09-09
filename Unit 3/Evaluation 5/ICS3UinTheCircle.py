import math

while True:
    R = int(input("Enter the radius of the circle (0 to quit): "))
    if R < 0:
        print("Radius cannot be negative. Please try again.")
        continue
    if R == 0:
        break
    a = int(input("Enter the x-coordinate of the point: "))
    b = int(input("Enter the y-coordinate of the point: "))
    c = int(input("Enter the x-coordinate of the circle's center: "))
    d = int(input("Enter the y-coordinate of the circle's center: "))

    # Calculate the distance between the point and the circle's center
    distance = math.sqrt((a - c) ** 2 + (b - d) ** 2)

    # Determine if the point is inside, outside, or on the circle
    if distance < R:
        print("The point is In the Circle.")
    elif distance > R:
        print("The point is Out of the Circle.")
    else:
        print("The point is On the Circle.")

    # Determine the quadrant of the point
    if a > 0 and b > 0:
        print("The point is in Quadrant I.")
    elif a < 0 and b > 0:
        print("The point is in Quadrant II.")
    elif a < 0 and b < 0:
        print("The point is in Quadrant III.")
    elif a > 0 and b < 0:
        print("The point is in Quadrant IV.")
    elif a == 0 and b > 0:
        print("The point is on the positive y-axis.")
    elif a == 0 and b < 0:
        print("The point is on the negative y-axis.")
    elif a > 0 and b == 0:
        print("The point is on the positive x-axis.")
    elif a < 0 and b == 0:
        print("The point is on the negative x-axis.")
    else:
        print("The point is at the origin.")