from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forward():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def move_clockwise():
    tim.rt(10)


def move_anticlockwise():
    # tim.lt(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear_screen():
    tim.reset()


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_anticlockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
