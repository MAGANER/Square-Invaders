from map import *
from time import sleep
from os import system
import keyboard
from hero import Hero
from bullet_manager import *
from checker import *
import monster_manager as mm
from question_generator import *
import bonus_manager as bm


def main():
    #####################################
    ###init game state
    ##################################
    #if restart
    bullets.clear() 
    mm.monsters.clear()
    
    field = init_field()
    hero = Hero()

    mm.init_monsters((6,0),(40,4))

    death,  victory, question= False, False,False
    frags = 0

    print('\033[?25l', end="")#hide cursor
    ################################

    while not death and not victory:
        system("cls||clear")

        #update clocks
        hero.tic()
        mm.tick_mtime()
        mm.tick_stime()
        bm.tick_bonus_time()
        bm.tick_movement_time()
        if not question:
            tick_qtime()
        
        chx, chy = hero.get_x(), hero.get_y()
        print_field(field,(chx,chy),bullets,mm.monsters,bm.bonuses)

        question = can_ask()
        if not question:
            if keyboard.is_pressed("left arrow") and can_move(chx-1,chy):
                hero.move_left()
            if keyboard.is_pressed("right arrow") and can_move(chx+1,chy):
                hero.move_right()
            if keyboard.is_pressed("space") and hero.can_shoot():
                bullets.append((chx,chy-1,True))
            if keyboard.is_pressed("S") and hero.can_shoot_super():
                poses = [(chx,chy-1,True),(chx-1,chy-1,True),(chx+1,chy-1,True)]
                for p in poses: bullets.append(p)

            frags = check_death((chx,chy),mm.monsters,hero)
            death = True if hero.health == 0 or mm.do_monsters_win() else False
        

            bm.check_time_to_generate_bonus()
            bm.move_bonuses()
            bm.check_hero_collides_bonuses(hero)

            if mm.monsters:
                mm.check_can_increase_shooting_freq()
                
                if mm.can_shoot(): mm.shoot(bullets)
                if mm.can_shoot_super(): mm.super_shoot(bullets)
                if mm.can_monsters_move(): mm.move_monsters()
            else:
                victory = True
            if frags != 0:
                hero.score += frags*hero.health
                frags = 0
                
            print(" "*15,"lives:{}".format(hero.health))
            print(" "*15,"score:{}".format(hero.score))

            hero.score += move_bullets() # add optional bonus score points if there are some of em
            sleep(0.1)
        
            if death:return False
            if victory: return True
        else:
            result = ask()
            if not result:
                if len(mm.monsters) > 10:
                    for n in range(10):
                        mm.shoot(bullets)
            else:
                hero.score = hero.score + 50
            question = False
                    
                

if __name__ == "__main__":
    try:
        result = main()
        system("cls||clear")
        choice = ""
        while True:
            if result:
                choice = input("You win! Nation of terminal is saved from hash-tags' invasion! Do you want to win again?(y/n)")
            else:
                choice = input("You died. Nation of terminal was conquered by hash-tags... Do you want to restart?(y/n)")

            if choice not in ["y","n"]: continue
            elif choice == "y": main()
            else: exit(0)
            
    except KeyboardInterrupt:
        system("cls||clear")
        exit(0)
