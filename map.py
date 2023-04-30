#game field rendering and creating module

class style():
    #BLACK = '\033[30m'
    RED = '\033[31m'
    #GREEN = '\033[32m'
    YELLOW = '\033[33m'
    #BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    #CYAN = '\033[36m'
    #WHITE = '\033[37m'
    END = "\33[0m"
def init_field(width, height):
    field = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(".")
        field.append(line)
    return field

def __print_hero(field,hero_pos):
    hy, hx  = hero_pos[1],hero_pos[0]
    field[hy][hx] = style.YELLOW+"@"+style.END
    field[hy][hx-1] = "."
    field[hy][hx+1] = "."
def __print_elements(field,bullets,monsters):
    for y in range(len(field)):
        line = field[y]
        for x in range(len(field[0])):
            if (x,y,False) in bullets:
                field[y][x] = style.MAGENTA+"*"+style.END
            elif (x,y,True) in bullets:
                field[y][x] = style.RED +"*"+style.END
            elif (x,y) in monsters:
                field[y][x] = "#"
            else:
                field[y][x] = "."
    
def print_field(field,hero_pos,bullets,monsters):
    print(" "*int((len(field[0])/3)) +"Square Invaders")

    __print_elements(field,bullets,monsters)
    __print_hero(field,hero_pos)

    for line in field:
        print("".join(line))
    print("\n")

def get_type(field,x,y):
    if field[y][x] == ".": return 0 #nothing
    elif field[y][x] == "@": return 1 #character
    elif field[y][x] == "*": return 2 #bullet
    elif field[y][x] == "#": return 3 #enemy

def set_val(field,x,y,val):
    field[y][x] = val
