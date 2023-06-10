from checker import *

bullets = []

def __collide(pos,bullets):
    for x,y, _ in bullets:
        if pos[0] == x and pos[1] == y:
            return (True,(x,y,False))
    return False
def move_bullets():
    counter = 0
    global bullets
    for b in bullets:
        mod = -1 if b[2] else 1
        x,y= b[0],b[1]+mod

        coll = __collide((x,y),bullets)
        result = False
        if type(coll) == type(False): result = False
        else: result = True

        if can_move(x,y) and not result:
            bullets[counter] = (x,y,True) if mod == -1 else (x,y,False)
        else:
            del(bullets[counter])
            if type(coll) == type(tuple()) and coll[1] in bullets:
                bullets.remove(coll[1])
        counter = counter + 1
            
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
