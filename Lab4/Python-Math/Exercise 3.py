import math
Sides = int(input())
Length_of_side = int(input())
Area = (Sides * (Length_of_side ** 2)) / 4 * math.tan(math.radians(180) / Sides)
print(round(Area))