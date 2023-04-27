from checker import *

bullets = []

def move_bullets():
    counter = 0
    global bullets
    for b in bullets:
        x,y= b[0],b[1]-1
        if can_move(x,y):
            bullets[counter] = (x,y)
        else:
            del(bullets[counter])
        counter = counter + 1
            
