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

def process_keyboard(hero_position, state,FIELD_HEIGHT=20):
    '''
      chx, chy - character's x and y position
    '''
    chx, chy = hero_position
    if keyboard.is_pressed("left arrow") and can_move(chx-1,chy,FIELD_HEIGHT):
        state.hero.move_left()
    if keyboard.is_pressed("right arrow") and can_move(chx+1,chy,FIELD_HEIGHT):
        state.hero.move_right()
    if keyboard.is_pressed("space") and state.hero.can_shoot():
        bullets.append((chx,chy-1,True))
        state.hero.sound_shoot()
    if keyboard.is_pressed("S") and state.hero.can_shoot_super():
        poses = [(chx,chy-1,True),(chx-1,chy-1,True),(chx+1,chy-1,True)]
        for p in poses: bullets.append(p)

def process_bonuses(state,FIELD_HEIGHT):
    bm.check_time_to_generate_bonus()
    bm.move_bonuses(FIELD_HEIGHT)
    bm.check_hero_collides_bonuses(state.hero)

    if bm.should_stop_monsters():
        bm.check_should_restart_monsters()

def process_monsters(state,FIELD_HEIGHT):
    if mm.monsters:
        mm.check_can_increase_shooting_freq()
        mm.check_can_decrease_time_to_move()
                
        if not bm.should_stop_monsters():
            if mm.can_shoot(): mm.shoot(bullets)
            if mm.can_shoot_super(): mm.super_shoot(bullets)
            if mm.can_monsters_move(): mm.move_monsters(FIELD_HEIGHT)
    else:
        state.victory = True

def process_misc_state(state,FIELD_HEIGHT=20):
    chx, chy = state.get_hero_position()

    terminal = True if FIELD_HEIGHT == 20 else False
    state.frags = check_death((chx,chy),mm.monsters,state.hero, terminal)
    state.death = True if state.hero.health == 0 or mm.do_monsters_win(FIELD_HEIGHT) else False
            
    if state.frags != 0:
        state.hero.score += state.frags*state.hero.health
        state.frags = 0
                
    state.hero.score += move_bullets(FIELD_HEIGHT) # add optional bonus score points if there are some of em
