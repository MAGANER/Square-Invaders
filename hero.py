import sys

not_classic = False
if len(sys.argv) > 1 and  sys.argv[1] != "classic":
    not_classic = True
    import pygame

class Hero(object):
    def __init__(self,y):
        self.__x = 30
        self.__y = y
        self.shooting_time_counter = 0
        self.health = 3
        self.score = 0
        self.shoot_sound = None
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def init_sound(self):
        if not not_classic:
            self.shoot_sound = pygame.mixer.Sound("assets/char_shoot.wav")
    def sound_shoot(self):
        if not not_classic and not self.shoot_sound is None:
            self.shoot_sound.play()
    def tic(self):
        self.shooting_time_counter = self.shooting_time_counter + 1
    def can_shoot(self):
        if self.shooting_time_counter > 5:
            self.shooting_time_counter = 0
            return True
        return False
    def can_shoot_super(self):
        if self.score >= 100:
            self.score -= 100
            return True
        return False
    def move_left(self):
        self.__x = self.__x -1
        return self.__x
    def move_right(self):
        self.__x = self.__x + 1
        return self.__x
