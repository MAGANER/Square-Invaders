
class Hero(object):
    def __init__(self):
        self.__x = 30
        self.__y = 19
        self.shooting_time_counter = 0
        self.health = 3
        self.score = 0
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

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
