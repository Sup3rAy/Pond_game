from turtle import Turtle


class Peddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.new_y = None
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def pedal_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def pedal_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
