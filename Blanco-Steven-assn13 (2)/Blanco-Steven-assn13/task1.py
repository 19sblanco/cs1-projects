from chessboard import Chessboard
import turtle


def main():
    startX, startY = eval(input("Enter a starting point: "))
    width = input("Input a width: ")
    height = input("Input a height: ")
    tr = turtle.Turtle()
    if width == "" and height == "":
       chessboard = Chessboard(tr, startX, startY)
    elif height == "":
       chessboard = Chessboard(tr, startX, startY, width=eval(width))
    elif width == "":
       chessboard = Chessboard(tr, startX, startY, height=eval(height))
    else:
       chessboard = Chessboard(tr, startX, startY, eval(width), eval(height))
    chessboard.draw()
    tr.hideturtle()
    turtle.done()
main()
