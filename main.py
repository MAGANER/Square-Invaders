from map import *
from time import sleep
from os import system
import keyboard
from hero import Hero
from bullet_manager import *
from monster_manager import *
from checker import *


field = init_field(FIELD_WIDTH,FIELD_HEIGHT)
hero = Hero()
init_monsters((10,10),(15,15))
print('\033[?25l', end="")#hide cursor
while True:
    system("cls||clear")
    hero.tic()
    
    chx, chy = hero.get_x(), hero.get_y()
    print_field(field,(chx,chy),bullets,monsters)

    if keyboard.is_pressed("left arrow") and can_move(chx-1,chy):
        hero.move_left()
    if keyboard.is_pressed("right arrow") and can_move(chx+1,chy):
        hero.move_right()
    if keyboard.is_pressed("space") and hero.can_shoot():
        bullets.append((chx,chy-1))

    move_monsters()
    move_bullets()
    sleep(0.1)
