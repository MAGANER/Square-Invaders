from checker import *
from random import choice, randint

monsters = []

def init_monsters(left_top_corner, bottom_right_corner):
    for y in range(left_top_corner[1],bottom_right_corner[1]):
        for x in range(left_top_corner[0],bottom_right_corner[0]):
            global monsters
            monsters.append((x,y))


def __get_sorted_x_poses():
    global monsters
    x_poses = [x for x,_ in monsters]
    x_poses.sort()
    return x_poses

def __get_leftest_monster_pos():
    return __get_sorted_x_poses()[0]
def __get_rightest_monster_pos():
    return __get_sorted_x_poses()[-1]

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


__time_to_shoot_super = 40
__super_shooting_time = 0

__super_shooting_range = (40,60)
def __decrease_range():
    global __super_shooting_range
    a = __super_shooting_range[0] - 2
    b = __super_shooting_range[1] - 2
    __super_shooting_range = (a,b)

__shooting_time = 0
def tick_stime():
    global __shooting_time
    global __super_shooting_time
    __shooting_time = __shooting_time + 1
    __super_shooting_time = __super_shooting_time + 1
def can_shoot():
    global __shooting_time
    if __shooting_time > 7:
        __shooting_time = 0
        return True
    return False
def can_shoot_super():
    global __super_shooting_time
    global __time_to_shoot_super
    if __super_shooting_time >= __time_to_shoot_super:
        __super_shooting_time = 0
        __time_to_shoot_super = randint(40,90)
        return True
    return False

def shoot(bullets):
    global monsters
    pos = choice(monsters)
    bullets.append((pos[0],pos[1],False))
def super_shoot(bullets):
    global monsters
    pos = choice(monsters)
    bullet_poses = [(pos[0],pos[1],False),(pos[0]-1,pos[1],False),(pos[0]+1,pos[1],False)]
    for bp in bullet_poses: bullets.append(bp)

def do_monsters_win():
    global monsters
    for m in monsters:
        if m[1] == 19:
            return True
    return False
__movement_counter = 0
def __reach_left():
    global monsters
    if __get_leftest_monster_pos() == -1:
        return True
    return False
def __reach_right():
    global monsters
    if __get_rightest_monster_pos() + 1 == FIELD_WIDTH:
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
            __decrease_range()
            
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
