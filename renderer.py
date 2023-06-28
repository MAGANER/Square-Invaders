import pygame
from Game import *

def prepare_text(font,text):
        return font.render(text, False, (255, 255, 0))
    
class InputBox:
    def __init__(self, x, y, w, h,font,text=""):
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.font = font
        self.rect = pygame.Rect(x, y, w, h)
        self.ready = False
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.ready = True
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        # Blit the text.
        screen.blit(prepare_text(self.font,self.text),(self.rect.x,self.rect.y))
    def clear(self):
        self.ready = False
        self.text = ""

class Renderer:
    def __init__(self):
        self.FIELD_HEIGHT = 30
        self.invader = pygame.image.load('SquareInvaders/assets/invader.png').convert_alpha()
        self.char = pygame.image.load("SquareInvaders/assets/char.png").convert_alpha()
        self.main_rects = [(10,5,835,5),(10,585,840,5),(10,5,5,580),(845,5,5,580)]
        self.question_rects = [(220,190,500,10),(220,400,500,10),(220,190,10,210),(720,190,10,220)]

        self.question_values = None

    def pp(self,val,offset=22):
        '''prepare position'''
        return offset+(val*16)
    
    def __draw_monsters(self,screen):
        dx = 1
        _,prevy = mm.monsters[0]
        for x,y  in mm.monsters:
            if y == prevy:
                dx +=1
            else:
                dx = 1
            screen.blit(self.invader,(self.pp(x)+dx,self.pp(y)))
            prevy =y
            
            
    def __draw_bullets(self,screen):
        for x,y,t in bullets:
            color = "red" if t else "magenta"         
            pygame.draw.circle(screen,color,pygame.Vector2(self.pp(x),self.pp(y)),radius=3)
        
    def __draw_character(self,screen,state):
        x,y = state.get_hero_position()
        #pygame.draw.rect(screen,"white",(self.pp(x,20),self.pp(y,20),8,8))
        screen.blit(self.char,(self.pp(x,20)-10,self.pp(y,20)))
        
    def __draw_bonuses(self,screen):
        for x,y,_ in bm.bonuses:
            key = random.choice(list(pygame.color.THECOLORS.keys()))
            pygame.draw.circle(screen,key,pygame.Vector2(self.pp(x),self.pp(y)),radius=4)
            
    def __draw_borders(self,screen,rects):
        for r in rects:
            pygame.draw.rect(screen,"green",r)
   
    def __draw_text(self,screen,text,pos):
        screen.blit(text, pos)
        
    def draw_game_session(self,screen,state,font):
            self.__draw_monsters(screen)
            self.__draw_bullets(screen)
            self.__draw_character(screen,state)
            self.__draw_bonuses(screen)

            self.__draw_text(screen,prepare_text(font,"lives:"+str(state.hero.health)),(350,510))
            self.__draw_text(screen,prepare_text(font,"score:"+str(state.hero.score)),(350,530))
            self.__draw_text(screen,prepare_text(font,"time: "+state.game_timer.get_time()),(335,550))
            self.__draw_borders(screen,self.main_rects)

    def draw_question(self,screen,font):
        pygame.draw.rect(screen,"black",(240,200,500,200))
        self.__draw_borders(screen,self.question_rects)
        a,b,_ = self.question_values
        self.__draw_text(screen,prepare_text(font,"please, answer the question: {} + {} = ?".format(a,b)),(260,240))
        
