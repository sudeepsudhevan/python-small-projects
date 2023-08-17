import turtle as t

import random

tim = t.Turtle()


# tim.shape("turtle")

# colors = ["red","green","blue","orange","purple","pink","yellow"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


t.colormode(255)  # change the color mode
tim.speed("fastest")

for directions in range(0, 361, 5):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(directions)
    
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/ size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading()+ size_of_gap)
# 
# draw_spirograph(5)
screen = t.Screen()

screen.exitonclick()
