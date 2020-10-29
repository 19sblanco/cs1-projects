import turtle as tr
import random


# configure turtle to draw quickly and set window size in function
def setup():
    tr.setup(1000, 800)
    tr.speed(0)

# draw rectangle pattern, calls draw rectangle
def drawRectanglePattern(centerX, centerY, offset, width, height,
                         count, rotation):
    # keep track of iterations
    i = 0

    # rotation
    tr.setheading(rotation)
    while i < count:
        # make turtle go to center point
        tr.penup()
        tr.setx(centerX)
        tr.sety(centerY)

        # set random color
        tr.pencolor(setRandomColor())

        # have it draw a rectangle with correct position
        tr.forward(offset)
        tr.pendown()
        setRandomColor()
        drawRectangle(width, height)
        tr.left(360 / count)

        # keep track of iterations
        i += 1

def drawRectangle(width, height):
    for i in range(2):
        tr.forward(width)
        tr.left(90)
        tr.forward(height)
        tr.left(90)

# draws circle pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    # keep track of iterations
    j = 0
    while j < count:
        # find starting point
        tr.penup()
        tr.setx(centerX)
        tr.sety(centerY)

        # set pen to random color
        tr.pencolor(setRandomColor())

        # have it draw circle in correct place
        tr.forward(offset)
        tr.right(90)
        tr.pendown()
        tr.circle(radius)
        tr.left(90)
        tr.left(360 / count)
         # add iteration
        j += 1

# draws a random number of patterns between 1 and 10
# draws random shapes and random amounts
def drawSuperPattern(num):
    for i in range(num):

        # have program randomly choose between drawing circle and rectangle patterns
        j = random.randint(0, 1)

        # draws circle pattern
        if j == 1:
            centerX = random.randint(-400, 400)
            centerY = random.randint(-300, 300)
            offset = random.randint(0, 50)
            radius = random.randint(10, 100)
            count = random.randint(2, 50)
            drawCirclePattern(centerX, centerY, offset, radius, count)
        # draws rectangle pattern
        else:
            centerX = random.randint(-400, 400)
            centerY = random.randint(-300, 300)
            offset = random.randint(-50, 50)
            width = random.randint(50, 200)
            height = random.randint(50, 200)
            count = random.randint(2, 50)
            rotation = random.randint(0, 359)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

# have turtle select random color
def setRandomColor():
    num = random.randint(0, 2)
    if num == 0:
        return "blue"
    elif num == 1:
        return "black"
    else:
        return "green"

# when user quits, keeps window open
def done():
    tr.done()

def reset():
    tr.clearscreen()
    tr.speed(0)

