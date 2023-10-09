#module provides ability to generate question that is one of the game feautures
import random
import sys

if len(sys.argv) > 1 and sys.argv[1] == "classic":
    import curses

__time_to_ask = 0
def tick_qtime():
    global __time_to_ask
    __time_to_ask = __time_to_ask + 1

def restart_asking_time():
    global __time_to_ask
    __time_to_ask = 0
def can_ask():
    '''check is it right time to ask question as a+b=?'''
    global __time_to_ask
    if __time_to_ask > 150:
        __time_to_ask = 0
        return True
    return False

def ask():
    '''generate question'''
    def get_question_data():
        question_type = False if random.randint(0,5) == 3 else True

        a = random.randint(1,100)
        b = random.randint(1,100)
        s = a+b if question_type else str(a)+str(b)
        a = a if question_type else '"{}"'.format(a)
        return a,b,s

    a,b,s= get_question_data()

    return get_question_data()

