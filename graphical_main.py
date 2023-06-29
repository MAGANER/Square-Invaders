from renderer import *

FIELD_HEIGHT = 30#it's evil state mutatation, but it's important!

def __run_game_session(screen,state):
    '''while hero is alive, monsters are alive and they don't reach the surface'''

    state.question = can_ask()
    if not state.question:
        process_keyboard(state.get_hero_position(),state,30)
        process_bonuses(state,FIELD_HEIGHT)
        process_misc_state(state,FIELD_HEIGHT)
        process_monsters(state)
            
        if state.death:return False
        if state.victory: return True
    else:
        return True
def __run_question_session(screen,question_box,renderer,state,question_box_timer):
    def check_answer():
        _,_,s = renderer.question_values
        return int(question_box.text) == int(s)
    def massive_shoot():
        if len(mm.monsters) > 10:
            for n in range(10):
                mm.shoot(bullets)

    if question_box.ready:
        if check_answer():
            state.hero.score = state.hero.score + 50
            state.question = False
        else:
            massive_shoot()
  
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((860,600))
    pygame.display.set_caption("Square Invaders")
    font = pygame.font.SysFont('Consolas', 16)

    question_box_timer = timer()
    
    clock = pygame.time.Clock()
    state = GameState(29)
    renderer = Renderer()

    question_box = InputBox(450,300,140,32,font)
    running = True
    draw_question = False

    while running:
        update_clocks(state)
        if draw_question: question_box_timer.tick()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if draw_question:
                question_box.handle_event(event)
        
        game_session = not state.death and not state.victory
        if game_session and not state.question:
            if __run_game_session(screen,state):
                state.question = True
                draw_question = True
                a,b,s = ask(True)
                renderer.question_values = (a,b,s)
        elif question_box.ready or (question_box_timer.get_seconds() > 10 and state.question):
            __run_question_session(screen,question_box,renderer,state,question_box_timer)
            state.question = False
            draw_question = False
            question_box_timer = timer()
            question_box.clear()
            print(state.death)


        screen.fill("black")
        if game_session: renderer.draw_game_session(screen,state,font)
        if draw_question:
            renderer.draw_question(screen,font)
            question_box.draw(screen)
        pygame.display.flip()

        
        clock.tick(5)
        
    pygame.quit()
