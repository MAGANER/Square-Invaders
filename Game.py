from GameState import *
from checker import *
import keyboard

def update_clocks(state):
    state.hero.tic()
    mm.tick_mtime()
    mm.tick_stime()
    bm.tick_bonus_time()
    bm.tick_movement_time()
    state.game_timer.tick()
    if bm.should_stop_monsters(): bm.tick_stop_time()
    if not state.question:
        tick_qtime()

def process_keyboard(hero_position, state):
    '''
      chx, chy - character's x and y position
    '''
    chx, chy = hero_position
    if keyboard.is_pressed("left arrow") and can_move(chx-1,chy):
        state.hero.move_left()
    if keyboard.is_pressed("right arrow") and can_move(chx+1,chy):
        state.hero.move_right()
    if keyboard.is_pressed("space") and state.hero.can_shoot():
        bullets.append((chx,chy-1,True))
    if keyboard.is_pressed("S") and state.hero.can_shoot_super():
        poses = [(chx,chy-1,True),(chx-1,chy-1,True),(chx+1,chy-1,True)]
        for p in poses: bullets.append(p)

def process_bonuses(state):
    bm.check_time_to_generate_bonus()
    bm.move_bonuses()
    bm.check_hero_collides_bonuses(state.hero)

    if bm.should_stop_monsters():
        bm.check_should_restart_monsters()

def process_monsters(state):
    if mm.monsters:
        mm.check_can_increase_shooting_freq()
        mm.check_can_decrease_time_to_move()
                
        if not bm.should_stop_monsters():
            if mm.can_shoot(): mm.shoot(bullets)
            if mm.can_shoot_super(): mm.super_shoot(bullets)
            if mm.can_monsters_move(): mm.move_monsters()
        else:
            state.victory = True

def process_misc_state(state):
    state.frags = check_death((chx,chy),mm.monsters,state.hero)
    state.death = True if state.hero.health == 0 or mm.do_monsters_win() else False
            
    if state.frags != 0:
        state.hero.score += state.frags*state.hero.health
        state.frags = 0
                
    state.hero.score += move_bullets() # add optional bonus score points if there are some of em
