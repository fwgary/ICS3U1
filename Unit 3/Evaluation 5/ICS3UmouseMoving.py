width = int(input("Enter the width of the screen: "))
height = int(input("Enter the height of the screen: "))
x_pos = int(input("Enter the starting X Position of the Mouse: "))
y_pos = int(input("Enter the starting Y Position of the Mouse: "))

while True:
    x_move = int(input("x movement: "))
    y_move = int(input("y movement: "))
    
    if x_move == 0 and y_move == 0:
        print("DONE")
        break
    
    # Update x position
    new_x = x_pos + x_move
    if new_x < 0:
        new_x = 0
    elif new_x > width - 1:
        new_x = width - 1
    
    # Update y position
    new_y = y_pos + y_move
    if new_y < 0:
        new_y = 0
    elif new_y > height - 1:
        new_y = height - 1
        
    print(f"The position is now ({new_x}, {new_y})")
    x_pos = new_x
    y_pos = new_y