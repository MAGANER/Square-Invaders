class timer:
    def __init__(self):
        self.__miliseconds = 0
        self.__seconds = 0
        self.__minutes = 0
        self.__hours = 0

    def tick(self):
        self.__miliseconds+= 1
        if self.__miliseconds == 5:
            self.__miliseconds = 0
            self.__seconds += 1

        if self.__seconds == 60:
            self.__miliseconds = 0
            self.__seconds = 0
            self.__minutes+= 1
        
        if self.__minutes == 60:
            self.__seconds = 0
            self.__minutes = 0
            self.__hours+= 1
    def get_time(self):
        return "{}:{}:{}".format(self.__seconds,self.__minutes,self.__hours)
