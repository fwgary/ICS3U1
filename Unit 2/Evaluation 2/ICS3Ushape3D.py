import math

def volume(a, b, c, d, e):
  """Calculates the volume of the structure.

  Args:
    a: The length of the base.
    b: The width of the base.
    c: The depth of the structure.
    d: The height of the structure.
    e: The radius of the circular arc.

  Returns:
    The volume of the structure.
  """

  # Calculate the volume of the rectangular prism
  volume_prism = a * b * d

  # Calculate the volume of the cylindrical segment
  volume_segment = (1/3) * math.pi * e**2 * (d - e)

  # Subtract the volume of the cylindrical segment from the volume of the prism
  volume = volume_prism - volume_segment

  return volume

def surface_area(a, b, c, d, e):
  """Calculates the surface area of the structure.

  Args:
    a: The length of the base.
    b: The width of the base.
    c: The depth of the structure.
    d: The height of the structure.
    e: The radius of the circular arc.

  Returns:
    The surface area of the structure.
  """

  # Calculate the area of the top and bottom faces
  area_top_bottom = 2 * a * b

  # Calculate the area of the front and back faces
  area_front_back = 2 * b * d

  # Calculate the area of the left and right faces
  area_left_right = 2 * a * d

  # Calculate the area of the curved surface
  area_curved = 2 * math.pi * e * c

  # Add up the areas of all the faces
  surface_area = area_top_bottom + area_front_back + area_left_right + area_curved

  return surface_area

# Get the dimensions from the user
a = float(input("Enter the length of the base (a): "))
b = float(input("Enter the width of the base (b): "))
c = float(input("Enter the depth of the structure (c): "))
d = float(input("Enter the height of the structure (d): "))
e = float(input("Enter the radius of the circular arc (e): "))

# Calculate the volume and surface area
volume = volume(a, b, c, d, e)
surface_area = surface_area(a, b, c, d, e)

# Print the results
print("The volume of the structure is:", volume)
print("The surface area of the structure is:", surface_area)