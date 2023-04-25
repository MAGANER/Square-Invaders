def init_field(width, height):
    field = []
    
    for y in range(height):
        line = []
        for x in range(width):
            line.append(".")
        field.append(line)
    return field
def print_field(field):
    print(" "*int((len(field[0])/3)) +"Square Invaders")
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
