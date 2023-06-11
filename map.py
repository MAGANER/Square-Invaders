#game field rendering and creating module
FIELD_WIDTH, FIELD_HEIGHT = 50, 20

class style():
    '''colors for terminals, supporting escape sequenceses'''
    #BLACK = '\033[30m'
    RED = '\033[31m'
    #GREEN = '\033[32m'
    YELLOW = '\033[33m'
    #BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    #CYAN = '\033[36m'
    #WHITE = '\033[37m'
    END = "\33[0m"

def init_field():
    '''generate matrix'''
    return [["."]*FIELD_WIDTH for _ in range(FIELD_HEIGHT)]

def __print_hero(field,hero_pos):
    hy, hx  = hero_pos[1],hero_pos[0]
    field[hy][hx] = style.YELLOW+"@"+style.END

def __print_bullets(field,color,pos):
    x,y = pos[0],pos[1]
    field[y][x] = color+"*"+style.END

def __print_elements(field,bullets,monsters):
    '''check field line by line and set correct data to show'''
    for y in range(FIELD_HEIGHT):
        line = field[y]
        for x in range(FIELD_WIDTH):
            if (x,y,False) in bullets:#enemy's bullet
                __print_bullets(field,style.MAGENTA,(x,y))
            elif (x,y,True) in bullets:#character's bullet
                __print_bullets(field,style.RED,(x,y))
            elif (x,y) in monsters:#regular monster
                field[y][x] = "#"
            else:#if it's not tuple, then it's empty space
                field[y][x] = "."
    
def print_field(field,hero_pos,bullets,monsters):
    print(" "*int((len(field[0])/3)) +"Square Invaders")

    #set elements and their position
    __print_elements(field,bullets,monsters)
    __print_hero(field,hero_pos)

    #print field line by line
    for line in field:
        print("".join(line))
    print("\n")

def get_type(field,x,y):
    if field[y][x] == ".": return 0 #nothing
    elif field[y][x] == "@": return 1 #character
    elif field[y][x] == "*": return 2 #bullet
    elif field[y][x] == "#": return 3 #enemy
