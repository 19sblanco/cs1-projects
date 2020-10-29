# chessboard module

# import assn10
'''
10 pts: Define drawChessboard() with appropriate parameters

This should draw the board outline, then call drawAllRectangles()
'''
import turtle
turtle.speed(0)

# draw chessboard, given the parameters
# drawChessboard function also calls drawAllRectangles function, too carry over parameter variables
def drawChessboard(startX,startY,width=250,height=250):
    turtle.penup()
    turtle.setx(startX)
    turtle.sety(startY)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    drawAllRectangles(startX, startY, width, height)

def drawRectangle(width, height):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.setheading(0)
    turtle.forward(width / 8)
    turtle.setheading(90)
    turtle.forward(height / 8)
    turtle.setheading(180)
    turtle.forward(width / 8)
    turtle.setheading(270)
    turtle.forward(height / 8)
    turtle.setheading(0)
    turtle.end_fill()

def drawRow(startX, startY, width, height):
    turtle.penup()
    turtle.setx(startX)
    turtle.sety(startY)
    turtle.pendown()
    for i in range(0, 4):
        drawRectangle(width, height)
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(width / 4)




def drawAllRectangles(startX, startY, width, height):
    for j in range(0, 2):
        # draws the first half of squares
        for i in range(0, 4):
            drawRow(startX, startY, width, height)
            startY += height / 4
        startY -= height # reset the height value
        # orient turtle to draw the remaining half of squares
        startY += height / 8
        startX += width / 8





