#module provides ability to create monsters, make them shoot, move
####CONTENT OF MODULE#####
#you can navigate, searching flag placed at the beginning of each block
#example: #n is flag, where n is number of block
##########################
#1 - init block
#2 - shooting block
#3 - boundaries checking block
#4 - movement block
##########################


from random import choice, randint
from map import FIELD_WIDTH,FIELD_HEIGHT

#1
################################################
####init block##################################
monsters = []

def init_monsters(left_top_corner, bottom_right_corner):
    '''generate monsters' position to fill subsquare of game field'''
    for y in range(left_top_corner[1],bottom_right_corner[1]):
        for x in range(left_top_corner[0],bottom_right_corner[0]):
            global monsters
            monsters.append((x,y))
def do_monsters_win(FIELD_HEIGHT):
    '''win if there is at least one monster who reaches the ground'''
    global monsters
    for m in monsters:
        if m[1]+1 == FIELD_HEIGHT-2:
            return True
    return False
#############################################

#2
#############################################
##########shooting block#####################
__time_to_shoot_super = 40 #(randomly generate in game process) when timer gets equal to this value, use triple shoot
__super_shooting_time = 0 #triple shooting timer
__super_shooting_range = (40,60) #time range of triple shooting
__shooting_time = 0 # regular shooting timer
__shooting_time_range = 8
__shooting_time_range_updated = False

def check_can_increase_shooting_freq():
    global __shooting_time_range
    global monsters
    global __shooting_time_range_updated

    if len(monsters)%8 == 0 and __shooting_time_range != 2 and not __shooting_time_range_updated:
        __shooting_time_range -= 1
        __shooting_time_range_updated = True
    
    if len(monsters)%4 != 0:
        __shooting_time_range_updated = False

def __decrease_range():
    '''everytime monsters move down, decrease range to use triple shooting ability'''
    global __super_shooting_range    
    da = __super_shooting_range[0] - 2  
    a =  da if da > 2 else 2

    db = __super_shooting_range[1] - 2 
    b =  db if db > 40 else 40

    __super_shooting_range = (a,b)

def tick_stime():
    global __shooting_time
    global __super_shooting_time
    __shooting_time = __shooting_time + 1
    __super_shooting_time = __super_shooting_time + 1
    
def can_shoot():
    global __shooting_time
    if __shooting_time > __shooting_time_range:
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
    '''add one bullet from random enemy'''
    global monsters
    pos = choice(monsters)
    bullets.append((pos[0],pos[1],False))
def super_shoot(bullets):
    ''' add 3 bullets from random enemy'''
    global monsters
    pos = choice(monsters)
    bullet_poses = [(pos[0],pos[1],False),(pos[0]-1,pos[1],False),(pos[0]+1,pos[1],False)]
    for bp in bullet_poses: bullets.append(bp)
############################################################

#3
############################################################
###boundaries checking block################################
def __get_sorted_x_poses():
    '''sort all x positions and return them as list'''
    global monsters
    x_poses = [x for x,_ in monsters]
    x_poses.sort()
    return x_poses

def __get_leftest_monster_pos():
    return __get_sorted_x_poses()[0]
def __get_rightest_monster_pos():
    return __get_sorted_x_poses()[-1]

def __reach_left():
    global monsters
    if __get_leftest_monster_pos() == 0:
        return True
    return False
def __reach_right():
    global monsters
    if __get_rightest_monster_pos() + 1 == FIELD_WIDTH-1:
        return True
    return False
def __reach_bottom(FIELD_HEIGHT):
    global monsters
    if monsters[-1][1] + 1 == FIELD_HEIGHT-2:
        return True
    return False
##################################

#4
##################################
###movement block#################
__movement_counter = 0 #increase when reach boundaries, and if it's 2, then move down
__movement_time = 0
__time_to_move = 2
__time_to_move_decreased = False

def check_can_decrease_time_to_move():
    global monsters
    global __time_to_move
    global __time_to_move_decreased
    y_pos = monsters[-1][1]
    if y_pos % 7 == 0 and not __time_to_move_decreased:
        __time_to_move -= 1
        __time_to_move_decreased = True
        
def tick_mtime():
    global __movement_time
    __movement_time = __movement_time + 1

def can_monsters_move():
    global __movement_time
    if __movement_time > __time_to_move:
        __movement_time = 0
        return True
    return False

def __move_monster(n,step_x,step_y):
    '''update position of single enemy'''
    global monsters
    updated = (monsters[n][0]+step_x,monsters[n][1]+step_y)
    monsters[n] = updated
    
def __move_monsters(step_x,step_y):
    ''' move all enemies'''
    for n in range(len(monsters)):
        __move_monster(n,step_x,step_y)

def move_monsters(FIELD_HEIGHT):
    global __movement_counter
    global monsters

    #move monster 1 step down
    if __movement_counter == 2 and not __reach_bottom(FIELD_HEIGHT):
            __move_monsters(0,1)
            __decrease_range()
            __movement_counter = 0

    #choose function associated with current movement direction
    checker = object()
    if __movement_counter == 0:
        checker = __reach_left
    elif __movement_counter == 1:
        checker = __reach_right
        
    if __movement_counter == 0 or __movement_counter == 1:
        if not checker():
            step = -1 if __movement_counter == 0 else 1
            __move_monsters(step,0)
        else:
            __movement_counter = __movement_counter + 1
    else:
        print("fuck, i'm here")
        __movement_counter = 2
        

#####################################################
