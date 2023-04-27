FIELD_WIDTH  = 60
FIELD_HEIGHT = 20

def can_move(new_x, new_y):
    return 0 < new_x < FIELD_WIDTH-1 and 0 < new_y < FIELD_HEIGHT
