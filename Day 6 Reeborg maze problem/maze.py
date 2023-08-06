def turn_right():
    turn_left()
    turn_left()
    turn_left()

#error fixed
while front_is_clear():
    move()
turn_left()
#above coded added    

def jump():
    if right_is_clear():
        turn_right()
        move()
    else:    
        turn_left()
    
    while wall_in_front() != True:
        if is_facing_north() and right_is_clear():
            turn_right()
            move()
        elif wall_on_right()!= True:
            turn_right()
            move()
        else:
            move()

while at_goal() != True:
    if front_is_clear():
        move()
    else:
        jump()
