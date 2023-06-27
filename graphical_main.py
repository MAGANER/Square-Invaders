from Game import *
import pygame



def __run_game_session(screen,state):
    '''while hero is alive, monsters are alive and they don't reach the surface'''

    state.question = can_ask()
    if not state.question:
        process_keyboard(state.get_hero_position(),state)
        #process_bonuses(state)
        process_monsters(state)
        #process_misc_state(state)
            
        if state.death:return False
        if state.victory: return True

def pp(val,offset=22):
    '''prepare position'''
    return offset+(val*16)
def __draw_field(screen):
    for y in range(FIELD_HEIGHT):
        y = pp(y)
        for x in range(FIELD_WIDTH):
            x = pp(x)
            pos = pygame.Vector2(x,y)
            pygame.draw.circle(screen, "green", pos,radius=2)
def __draw_monsters(screen):
    for x,y in mm.monsters:
        pygame.draw.rect(screen,"red",(pp(x,20),pp(y,20),20,20))
def __draw_game_session(screen):
    __draw_field(screen)
    __draw_monsters(screen)
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((840,500))
    pygame.display.set_caption("Square Invaders")
    
    clock = pygame.time.Clock()
    state = GameState()
    running = True

    while running:
        update_clocks(state)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_session = not state.death and not state.victory
        if game_session:
            __run_game_session(screen,state)

        screen.fill("black")
        
        if game_session: __draw_game_session(screen)
        
        pygame.display.flip()
        clock.tick(5)
        
    pygame.quit()
        
