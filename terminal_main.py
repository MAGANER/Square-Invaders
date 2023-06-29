
from time import sleep
from os import system
from Game import *

def main():
    #####################################
    ###init game state
    ##################################
    state = GameState(19)
    
    
    print('\033[?25l', end="")#hide cursor
    ################################

    while not state.death and not state.victory:
        system("cls||clear")
        update_clocks(state)

        
        chx, chy = state.hero.get_x(), state.hero.get_y()
        print_field(state.field,(chx,chy),bullets,mm.monsters,bm.bonuses)
        print(" "*15,"lives:{}".format(state.hero.health))
        print(" "*15,"score:{}".format(state.hero.score))
        print(" "*12,"time - {}".format(state.game_timer.get_time()))

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
            if not result:
                if len(mm.monsters) > 10:
                    for n in range(10):
                        mm.shoot(bullets)
            else:
                state.hero.score = state.hero.score + 50
            state.question = False

def finish():
    print("\033[?25h",end="")
    exit(0)
    
def run_game():
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
            else: finish()
            
    except KeyboardInterrupt:
        system("cls||clear")
        finish()
