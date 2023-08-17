import turtle as t

import random

tim = t.Turtle()


# tim.shape("turtle")

# colors = ["red","green","blue","orange","purple","pink","yellow"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


t.colormode(255)  # change the color mode

directions = [0, 90, 180, 270]

tim.speed("fastest")
tim.pensize(10)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))







screen = t.Screen()

screen.exitonclick()
