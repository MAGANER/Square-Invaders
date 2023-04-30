from checker import *
from random import choice

monsters = []

def init_monsters(left_top_corner, bottom_right_corner):
    for y in range(left_top_corner[1],bottom_right_corner[1]):
        for x in range(left_top_corner[0],bottom_right_corner[0]):
            global monsters
            monsters.append((x,y))

__movement_time = 0

def tick_mtime():
    global __movement_time
    __movement_time = __movement_time + 1

def can_monsters_move():
    global __movement_time
    if __movement_time > 2:
        __movement_time = 0
        return True
    return False
        
__shooting_time = 0
def tick_stime():
    global __shooting_time
    __shooting_time = __shooting_time + 1
def can_shoot():
    global __shooting_time
    if __shooting_time > 7:
        __shooting_time = 0
        return True
    return False

def shoot(bullets):
    global monsters
    pos = choice(monsters)
    bullets.append((pos[0],pos[1],False))

def do_monsters_win():
    global monsters
    for m in monsters:
        if m[1] == 19:
            return True
    return False
__movement_counter = 0
def __reach_left():
    global monsters
    if monsters[0][0] -1 == -1:
        return True
    return False
def __reach_right():
    global monsters
    if monsters[-1][0] + 1 == FIELD_WIDTH:
        return True
    return False
def __reach_bottom():
    global monsters
    if monsters[-1][1] + 1 == 18:
        return True
    return False

def __move_monster(n,step_x,step_y):
    global monsters
    updated = (monsters[n][0]+step_x,monsters[n][1]+step_y)
    monsters[n] = updated
    
def __move_monsters(step_x,step_y):
    for n in range(len(monsters)):
        __move_monster(n,step_x,step_y)

def move_monsters():
    global __movement_counter
    global monsters

    if __movement_counter == 2 and not __reach_bottom():
            __move_monsters(0,1)
            
    if __movement_counter == 2:
        __movement_counter = 0
        
    checker = object()
    if __movement_counter == 0:
        checker = __reach_left
    if __movement_counter == 1:
        checker = __reach_right
        
    if not checker():
        step = -1 if __movement_counter == 0 else 1
        __move_monsters(step,0)
    else:
        __movement_counter = __movement_counter + 1
