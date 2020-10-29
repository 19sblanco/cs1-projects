import turtle
class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True
    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()
    def is_smile(self):
        if self.__smile:
            return True
        else:
            return False
    def is_happy(self):
        if self.__happy:
            return "yellow"
        else:
            return "red"
    def is_dark_eyes(self):
        if self.__dark_eyes:
            return "black"
        else:
            return "blue"
    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()
    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()
    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()
    def __draw_head(self):
        turtle.penup()
        turtle.goto(0, -100)
        turtle.pendown()
        turtle.fillcolor(self.is_happy())
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
    def __draw_eyes(self):
        x_coordinate = -35
        y_coordinate = 40
        for i in range(2):
            turtle.penup()
            turtle.setx(x_coordinate)
            turtle.sety(y_coordinate)
            turtle.pendown()
            turtle.fillcolor(self.is_dark_eyes())
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            x_coordinate += 70
    def __draw_mouth(self):
        if self.is_smile():
             turtle.penup()
             turtle.setx(0)
             turtle.sety(-45)
             turtle.pendown()
             turtle.pensize(8)
             turtle.circle(75, 60)
             turtle.penup()
             turtle.setx(0)
             turtle.sety(-45)
             turtle.pendown()
             turtle.pensize(8)
             turtle.setheading(180)
             turtle.circle(-75, 60)
             turtle.setheading(0)
             turtle.pensize(1)
        else:
            turtle.penup()
            turtle.setx(0)
            turtle.sety(-25)
            turtle.pendown()
            turtle.pensize(8)
            turtle.circle(-75, 60)
            turtle.penup()
            turtle.setx(0)
            turtle.sety(-25)
            turtle.pendown()
            turtle.pensize(8)
            turtle.setheading(180)
            turtle.circle(75, 60)

