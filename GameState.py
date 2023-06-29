from timer import *
from hero import Hero
from map import *
import monster_manager as mm
from bullet_manager import *
import bonus_manager as bm
from question_generator import *

class GameState:
    def __init__(self,hero_y):
        bullets.clear()
        mm.monsters.clear()

        mm.init_monsters((6,0),(40,4))
        self.field = init_field()
        self.hero = Hero(hero_y)
        self.game_timer = timer()


        self.death, self.victory, self.question = False, False, False
        self.frags = 0

    def get_hero_position(self):
        return self.hero.get_x(), self.hero.get_y()
