import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")


# tim.color("DarkRed")


# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
def random_color():
    R = 0
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tim.color(R, G, B)


turtle.colormode(255)

# side = 2
# for i in range(8):
#     side += 1
#     random_color()
#     for j in range(side):
#         tim.forward(100)
#         tim.right(360 / side)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,11):
    draw_shape(shape_side)
    random_color()

screen = Screen()

screen.exitonclick()
