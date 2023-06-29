from random import randint,choice
from checker import *
import hero
bonuses = []


__stop_monsters_for_10_seconds = False
__stop_time_counter = 0
def tick_stop_time():
    global __stop_time_counter
    __stop_time_counter += 1
def should_stop_monsters():
    global __stop_monsters_for_10_seconds
    return __stop_monsters_for_10_seconds
def check_should_restart_monsters():
    global __stop_time_counter
    global __stop_monsters_for_10_seconds
    if __stop_time_counter > 60:
        __stop_monsters_for_10_seconds = False


def add_h(hero): hero.health+=1
def add_s(hero): hero.score+=10
def del_h(hero): 
    hero.health+=1
    hero.score+=15
def stop_m(hero):
    global __stop_monsters_for_10_seconds 
    __stop_monsters_for_10_seconds = True
types = (add_h, add_s,del_h, stop_m)

__time_to_generate_bonus = 5
def tick_bonus_time():
    global __time_to_generate_bonus
    __time_to_generate_bonus+= 1

def check_time_to_generate_bonus():
    global __time_to_generate_bonus
    global bonuses
    if __time_to_generate_bonus > 170 and randint(0,1) == 1:
        x,y = randint(4,19), randint(0,6)
        bonuses.append((x,y,choice(types)))
        __time_to_generate_bonus = 0

__movement_time_counter = 3
def tick_movement_time():
    global __movement_time_counter
    __movement_time_counter+= 1

def move_bonuses(FIELD_HEIGHT):
    global __movement_time_counter
    if __movement_time_counter > 3:
        __movement_time_counter = 0
        for i,val in enumerate(bonuses):
            if can_move(val[0],val[1],FIELD_HEIGHT):
                bonuses[i] = (val[0],val[1]+1,val[2])
            else:
                del(bonuses[i])

def check_hero_collides_bonuses(hero):
    for i, val in enumerate(bonuses):
        x,y = val[0], val[1]
        eq_pos = hero.get_x() == x and hero.get_y() == y
        if eq_pos:
            val[2](hero)
            del(bonuses[i]) 
