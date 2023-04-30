from map import *
from time import sleep
from os import system
import keyboard
from hero import Hero
from bullet_manager import *
from checker import *
import monster_manager as mm

def main():
    bullets.clear() #if restart
    mm.monsters.clear()
    
    field = init_field(FIELD_WIDTH,FIELD_HEIGHT)
    hero = Hero()
    mm.init_monsters((10,10),(15,15))
    death = False

    print('\033[?25l', end="")#hide cursor
    while not death:
        system("cls||clear")
        hero.tic()
        mm.tick_mtime()
        mm.tick_stime()
    
        chx, chy = hero.get_x(), hero.get_y()
        print_field(field,(chx,chy),bullets,mm.monsters)
        if keyboard.is_pressed("left arrow") and can_move(chx-1,chy):
            hero.move_left()
        if keyboard.is_pressed("right arrow") and can_move(chx+1,chy):
            hero.move_right()
        if keyboard.is_pressed("space") and hero.can_shoot():
            bullets.append((chx,chy-1,True))

        check_death((chx,chy),mm.monsters,hero)
        death = True if hero.health == 0 else False
        
        if mm.can_shoot(): mm.shoot(bullets)
        if mm.can_monsters_move(): mm.move_monsters()

        print(" "*15,"lives:{}".format(hero.health))
        print(" "*15,"score:{}".format(hero.score))
        move_bullets()
        sleep(0.1)

if __name__ == "__main__":
    try:
        main()
        system("cls||clear")
        choice = ""
        while True:
            choice = input("You died. Nation of terminal was conquered by hash-tags... Do you want to restart?(y/n)")
            if choice not in ["y","n"]: continue
            elif choice == "y": main()
            else: break
            
    except KeyboardInterrupt:
        system("cls||clear")
        exit(0)
