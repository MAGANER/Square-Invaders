
from renderer import *

FIELD_HEIGHT = 30#it's evil state mutatation, but it's important!

def __run_game_session(screen,state):
    '''while hero is alive, monsters are alive and they don't reach the surface'''

    state.question = can_ask()
    if not state.question:
        process_keyboard(state.get_hero_position(),state,30)
        process_bonuses(state)
        process_misc_state(state,FIELD_HEIGHT)
        process_monsters(state)
            
        if state.death:return False
        if state.victory: return True

  
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((860,600))
    pygame.display.set_caption("Square Invaders")
    font = pygame.font.SysFont('Consolas', 16)
    
    clock = pygame.time.Clock()
    state = GameState(29)
    renderer = Renderer()
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
        
        if game_session: renderer.draw_game_session(screen,state,font)
        
        pygame.display.flip()
        clock.tick(5)
        
    pygame.quit()
        
