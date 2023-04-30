from checker import *

monsters = []

def init_monsters(left_top_corner, bottom_right_corner):
    for y in range(left_top_corner[1],bottom_right_corner[1]):
        for x in range(left_top_corner[0],bottom_right_corner[0]):
            global monsters
            monsters.append((x,y))

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
            
        
   
        

    


