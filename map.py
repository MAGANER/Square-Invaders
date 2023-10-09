import curses
import GameState
from quit_after import *

#game field rendering and creating module
FIELD_WIDTH, FIELD_HEIGHT = 50, 20

class style():
    '''colors for terminals, supporting escape sequenceses'''
    #BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    #BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    #CYAN = '\033[36m'
    #WHITE = '\033[37m'
    END = "\33[0m"


stdscr = None
def init():
    global stdscr
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)

def quit():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    curses.curs_set(1)
def refresh():
    global stdscr
    stdscr.clear()
    
    
def init_field():
    '''generate matrix'''
    return [["."]*FIELD_WIDTH for _ in range(FIELD_HEIGHT)]


def __print_elements(field,bullets,monsters,bonuses):
    '''check field line by line and set correct data to show'''

    bonuses_poses = [(x,y) for x,y,_ in bonuses]
    for y in range(FIELD_HEIGHT):
        line = field[y]
        for x in range(FIELD_WIDTH):
            if (x,y) in bonuses_poses:
                stdscr.addstr(y,x,"?")
            elif (x,y,False) in bullets:#enemy's bullet
                stdscr.addstr(y,x,"*")
            elif (x,y,True) in bullets:#character's bullet
                stdscr.addstr(y,x,"*")
            elif (x,y) in monsters:#regular monster
                stdscr.addstr(y,x,"#")
            else:#if it's not tuple, then it's empty space
                stdscr.addstr(y,x,".")
    
def print_field(field,hero_pos,bullets,monsters,bonuses):
    print(" "*int((len(field[0])/3)) +"Square Invaders")

    #set elements and their position
    __print_elements(field,bullets,monsters,bonuses)
    stdscr.addstr(hero_pos[1],hero_pos[0],"@")

    #print field line by line
    for line in field:
        print("".join(line))
    print("\n")

def cprint_field(field,hero_pos,bullets,monsters,bonuses):
    for y in range(0,FIELD_HEIGHT):
        for x in range(0,FIELD_WIDTH):
            stdscr.addstr(y,x,".")

    __print_elements(field,bullets,monsters,bonuses)
    stdscr.addstr(hero_pos[1],hero_pos[0],"@")

def print_state(state):
    stdscr.addstr(20,20,"health:"+str(state.hero.health))
    stdscr.addstr(21,20,"score:"+str(state.hero.score))
    stdscr.addstr(22,18,"time - "+ str(state.game_timer.get_time()))

@exit_after(5)
def print_question(a,b,c):
    stdscr.addstr(23,18,"please, answer the question {} + {} = ?".format(a,b))
    curses.echo()
    curses.curs_set(1)
    s = stdscr.getstr(24,15,4)
    curses.curs_set(0)
    return s == c

def update():
    stdscr.refresh()    
    
def get_type(field,x,y):
    if field[y][x] == ".": return 0 #nothing
    elif field[y][x] == "@": return 1 #character
    elif field[y][x] == "*": return 2 #bullet
    elif field[y][x] == "#": return 3 #enemy
