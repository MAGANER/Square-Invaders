from checker import *
from time import sleep

bullets = []

def check_bullet_collision(bull_data,bullets):
    _x,_y, _bul_type = bull_data
    for key, val in enumerate(bullets):
        x,y, bul_type = val

        eq = _x == x and _y == y and bul_type != _bul_type
        if eq:
            bul_type = not bullets[key][2]
            mod = 1 if bul_type else -1
            del(bullets[key])
            bullets.remove((x,y+mod,bul_type))
            return True
    return False
def move_bullets(FIELD_HEIGHT):
    add_score = 0 #if hero's bullet destroys monster's one
    
    global bullets
    for counter, b in enumerate(bullets):
        mod = -1 if b[2] else 1
        x,y= b[0],b[1]+mod

        if check_bullet_collision((x,y,b[2]),bullets):
            add_score += 10
            continue
        
        if can_move(x,y,FIELD_HEIGHT):
            bullets[counter] = (x,y,True) if mod == -1 else (x,y,False)
        else:
            del(bullets[counter])

    return add_score
            
def check_death(hero_pos, monsters_poses,hero):
    counter = 0
    frag_counter = 0
    for b in bullets:
        if (b[0],b[1]) in monsters_poses and b[2]:
            del(bullets[counter])
            monsters_poses.remove((b[0],b[1]))
            frag_counter = frag_counter + 1
        if (b[0],b[1]) == hero_pos: hero.health = hero.health - 1
        counter = counter + 1
    return frag_counter
