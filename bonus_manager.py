from random import randint,choice
import hero
bonuses = []

def add_h(hero): hero.health+=1
def add_s(hero): hero.score+=10
def del_h(hero): 
    hero.health+=1
    hero.score+=15
types = (add_h, add_s,del_h)

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

def move_bonuses():
    global __movement_time_counter
    if __movement_time_counter > 3:
        __movement_time_counter = 0
        for i,val in enumerate(bonuses):
            if val[1]+1 < 50:
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