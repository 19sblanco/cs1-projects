'''
    This program will allow you to enter in the number of sides
    of a regular polygon and the length of each side then will
    calculate the area of that polygon
'''
'''
area = (n * s **2) / (4 * tan(pi / n))
s is the length of a side
n is the number of sides
'''
# 1. Have users enter in the number of sides of their polygon
# 2. Have users enter in the length of each side
# 3. take those inputs and enter them in the area formula

import math

# impliment code
# Have users enter in the data, # of sides, length of sides
sideLength = float(input("Enter in the side length: "))
numberOfSides = float(input("Enter in the number of sides: "))

# redefine tangent and pi
tan = math.tan
pi = math.pi

# calculate area
area = (numberOfSides * sideLength**2) / (4 * tan(pi / numberOfSides))

print(area)

#test1: # of sides 5, side length 6.5
#failed converted int to float