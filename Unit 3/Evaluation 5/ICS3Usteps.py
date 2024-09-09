import random

# Generate random steps forward and backward
forward_steps = random.randint(2, 20)
backward_steps = random.randint(2, forward_steps - 1)

# Generate random total steps
total_steps = random.randint(10, 85)

# Initialize the motion string and the current position
motion = ""
position = 0

# Simulate the motion
while total_steps > 0:
    for _ in range(forward_steps):
        motion += "F"
        position += 1
        total_steps -= 1
        if total_steps == 0:
            break
    for _ in range(backward_steps):
        motion += "B"
        position -= 1
        total_steps -= 1
        if total_steps == 0:
            break

# Display the motion and the final position
print(motion + " = " + str(position) + " Steps from the start")