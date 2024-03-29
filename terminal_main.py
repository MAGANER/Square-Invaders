from time import sleep
from os import system
import os
import importlib
from Game import *
import curses

def main():
    #####################################
    ###init game state
    ##################################
    state = GameState(19)
    
    init()
    ################################

    while not state.death and not state.victory:
        update_clocks(state)

        
        chx, chy = state.hero.get_x(), state.hero.get_y()
        cprint_field(state.field,(chx,chy),bullets,mm.monsters,bm.bonuses)
        print_state(state)

        state.question = can_ask()
        if not state.question:
            process_keyboard(state.get_hero_position(),state)
            process_bonuses(state,FIELD_HEIGHT)
            process_monsters(state,FIELD_HEIGHT)
            process_misc_state(state)
           
            if state.death:return False
            if state.victory: return True

            sleep(0.1)        
        else:
            result = ask()
            if not print_question(*result):
                if len(mm.monsters) > 10:
                    for n in range(10):
                        mm.shoot(bullets)
            else:
                state.hero.score = state.hero.score + 50
            state.question = False

        update()
        refresh()

    

def finish():
    print("\033[?25h",end="")
    exit(0)
    
def run_game():
    try:
        result = main()
        quit()
        if os.name == "nt":
            system("cls")
        else:
            system("clear")
        choice = ""
        while True:
            if result:
                choice = input("You win! Nation of terminal is saved from hash-tags' invasion! Do you want to win again?(y/n)")
            else:
                choice = input("You died. Nation of terminal was conquered by hash-tags... Do you want to restart?(y/n)")

            if choice not in ["y","n"]:
                #reset state
                module = os.path.basename(__file__)[:-3]
                module = importlib.import_module(module)
                importlib.reload(module)                 
                continue
            elif choice == "y": main()
            else: finish()
            
    except KeyboardInterrupt:
        system("cls||clear")
        finish()
        quit()
