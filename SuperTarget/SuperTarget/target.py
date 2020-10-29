import turtle
import random

# reset
def reset():
    # erase all of the targets
    turtle.reset()
    turtle.speed(0)


# setup
def setup():
    # set the speed of turtle
    turtle.speed(0)
    # set the window size to 1000 x 800
    turtle.setup(1000, 800)

# drawSuperTarget
def drawSuperTarget(num): # param - the number of targets to draw
    # loop the number of targets to draw times
    for i in range(num):
        # random: radius, location, rings
        centerX = random.randint(-500, 500)
        centerY = random.randint(-400, 400)
        radius = random.randint(5, 50)
        rings = random.randint(1, 10)

        # draw a target -
        drawTarget(centerX, centerY, radius, rings)

# drawTarget()
    # param -
    # center X point
    # center Y point
    # radius value - default to 50
    # number of rings - default to 3
def drawTarget(centerX, centerY, radius=50, rings=3):
    # loop the number of rings times - start at largest to smallest
    for i in range(rings, 0, -1):
        # select a color
        if i % 2 == 0:
            color = 'blue'
        else:
            color = 'red'

        # ring number * radius is the circles radius
        # move number * radius in the -y direction
        # draw a circle
        drawCircle(centerX, centerY - i * radius, i * radius, color)


# drawCircle()
    # param -
        # start X point
        # start Y point
        # radius
        # color
def drawCircle(startX, startY, radius, color):
    # Draw the circle
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(startX, startY)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()


# done()
def done():
    turtle.done()

