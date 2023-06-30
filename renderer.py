import pygame
from Game import *

def prepare_text(font,text,color=(255,255,0)):
        return font.render(text, False, color)
    
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
        self.invader = self.__load_image('invader.png')
        self.char = self.__load_image("char.png")
        self.main_rects = [(10,5,835,5),(10,585,840,5),(10,5,5,580),(845,5,5,580)]
        self.question_rects = [(220,190,500,10),(220,400,500,10),(220,190,10,210),(720,190,10,220)]

        self.question_values = None

    def __load_image(self,name):
            path1 = "SquareInvaders/assets/"+name
            path2 = "assets/"+name
            
            image = None
            load = lambda p:pygame.image.load(p).convert_alpha()
            try:
                image = load(path1)
            except FileNotFoundError:
                try:
                    image = load(path2)
                except FileNotFoundError:
                    print("can not load {} and {}.".format(path1,path2))
                    exit(-1)
            return image

                             
    def pp(self,val,offset=22):
        '''prepare position'''
        return offset+(val*16)
    
    def __draw_monsters(self,screen):
        if len(mm.monsters) == 0:
                return

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
            y_pos = self.pp(y)+10 if not t else self.pp(y)
            x_pos = self.pp(x)+5 if not t else self.pp(x)+5
            pygame.draw.circle(screen,color,pygame.Vector2(x_pos,y_pos),radius=3)
        
    def __draw_character(self,screen,state):
        x,y = state.get_hero_position()
        #pygame.draw.rect(screen,"white",(self.pp(x,20),self.pp(y,20),8,8))
        screen.blit(self.char,(self.pp(x,20)-5,self.pp(y,20)))
        
    def __draw_bonuses(self,screen):
        for x,y,_ in bm.bonuses:
            key = random.choice(list(pygame.color.THECOLORS.keys()))
            pygame.draw.circle(screen,key,pygame.Vector2(self.pp(x),self.pp(y)),radius=4)
            
    def __draw_borders(self,screen,rects,color="green"):
        for r in rects:
            pygame.draw.rect(screen,color,r)
   
    def __draw_text(self,screen,text,pos):
        screen.blit(text, pos)
        
    def __draw_finish_screen(self,screen,font,label, second_label):
        self.__draw_text(screen,prepare_text(font,label),(360,240))
        self.__draw_text(screen,prepare_text(font,"press"),(180,260))
        self.__draw_text(screen,prepare_text(font, "Y",(255,0,0)),(235,260))
        self.__draw_text(screen,prepare_text(font,second_label),(245,260))
        self.__draw_borders(screen,self.main_rects)
    def draw_death_screen(self,screen,font):
            self.__draw_finish_screen(screen,font,"YOU DIED?"," to see the answer and be careful with the stone,Sysyphus.")
    def draw_victory_screen(self,screen,font):
            self.__draw_finish_screen(screen,font,"YOU WIN."," to see what's next and be careful with the stone,Sysyphus.")
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
        pygame.draw.rect(screen,"black",(230,200,500,200))
        self.__draw_borders(screen,self.question_rects)
        a,b,_ = self.question_values
        self.__draw_text(screen,prepare_text(font,"please, answer the question: {} + {} = ?".format(a,b)),(260,240))
        
