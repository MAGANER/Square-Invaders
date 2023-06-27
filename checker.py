def can_move(new_x, new_y,FIELD_HEIGHT):
    #49 = FIELD_WIDTH - 1
    return 0 < new_x < 49 and 0 < new_y < FIELD_HEIGHT
