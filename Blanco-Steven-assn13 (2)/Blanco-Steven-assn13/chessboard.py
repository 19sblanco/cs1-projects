import turtle as tr

tr.speed(0)
class Chessboard:
    # define instant variables
    def __init__(self, tr, startX=0, startY=0, width=250, height=250):
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height
    # draws outline of chessboard
    def __drawChessboard(self):
        tr.penup()
        tr.setx(self.__startX)
        tr.sety(self.__startY)
        tr.pendown()
        for i in range(2):
            tr.forward(self.__width)
            tr.left(90)
            tr.forward(self.__height)
            tr.left(90)
        self.__drawAllRectangles()
    # draws all black squares in the chessboard
    def __drawAllRectangles(self):
        for k in range(1):
            for j in range(4):
                tr.setx(self.__startX)
                tr.sety(self.__startY)
                self.__drawRow()
                self.__startY += self.__height / 4
            self.__startX += self.__width / 8
            self.__startY -= self.__height
            self.__startY += self.__height / 8
    # draws a rectangle
    def __drawRectangle(self):
        tr.begin_fill()
        for i in range(2):
            tr.forward(self.__width / 8)
            tr.left(90)
            tr.forward(self.__height / 8)
            tr.left(90)
        tr.end_fill()
    # draws a row of rectangles
    def __drawRow(self):
        for i in range(4):
            tr.pendown()
            self.__drawRectangle()
            tr.penup()
            tr.forward(self.__width / 4)
    # draws the whole chessboard
    def draw(self):
        self.__drawChessboard()
        self.__drawAllRectangles()