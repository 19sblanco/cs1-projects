# steven blanco
# CS 1400 - 3
# assn 7

'''
requirement specification:
prompt user to enter in the center coordinates and radii of two circles and
determin whether the second circle is inside the first or if they just overlap
'''

'''
system analysis:
distance formula
    distance = sqrt((y2 - y1) **2 + (x2 - x1) ** 2)
if second circle inside first circle
    value = distance <= abs(r1 - r2)
if second circle overlaps first circle
    value = distance <= abs(r1 + r2)
if neither
    value = distance > abs(r1 + r2)
'''

'''
system design:
1.
1. explain program to user
2. prompt user to enter in coordinates of first circle and second circle
3. get the radius of both circles
4. find the distance between the to centers of the circle
5. use if statements to determine whether they overlap all the way or just 
some of the way
6. print output
'''

#code

'''
test 1: passed
    circle 1:
    (0, 0) r = 5
    circle 2:
    (0, 2) r = 2
    expected output: inside
test 2: failed: changed the <= to < on line 72
    circle 1:
    (0, 0) r = 2
    circle 2:
    (-4, 3) r = 3
    expected output: they don't overlap
'''

import math

#explain program to user
print("This program will allow you to enter the coordinates and radii of two\n cirlces and will tell you if the second circle is inside the first circle,\n if they overlap or neither")

# prompt user to enter in coordinates of both circles and radii
# store radii value as circle1R and circle2R
circleX1 = float(input("Enter in the x-coordinate of the first circle: "))
circleY1 = float(input("Enter in the y-coordinate of the first circle: "))
circleR1 = float(input("Enter in the radius of the first circle: "))
circleX2 = float(input("Enter in the x-coordiante of the second circle: "))
circleY2 = float(input("Enter in the y-coordinate of the second circle: "))
circleR2 = float(input("Enter in the radius of the second circle: "))

# find distance between the center of the two circles and store as distance
distance = math.sqrt((circleY2 - circleY1) **2 + (circleX2 - circleX1) ** 2)

# use if statements to determine which circle is inside one another
# then determine which circle is inside the other
# complete it with determining if they are the same circle
if distance <= abs(circleR1 - circleR2):
    if circleR1 > circleR2:
        print("circle2 is inside circle1")
    elif circleR2 > circleR1:
        print("circle1 is inside circle2")
    elif circleR2 == circleR1:
        print("These circles are the same")

# use if statements to determine if they are overlapping
# use else statement to determine if they don't
elif distance < circleR1 + circleR2:
    print("They overlap eachother")
    
# print statement in event they don't overlap at all
else:
    print("They do not overlap at all")