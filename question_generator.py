#module provides ability to generate question that is one of the game feautures
import random
from inputimeout import inputimeout, TimeoutOccurred

def flush_input():
    try:
        #TODO:this solution doesn't work for windows properly
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

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

def ask(graphical = False):
    '''generate question'''
    def get_question_data():
        question_type = False if random.randint(0,5) == 3 else True

        a = random.randint(1,100)
        b = random.randint(1,100)
        s = a+b if question_type else str(a)+str(b)
        a = a if question_type else '"{}"'.format(a)
        return a,b,s

    a,b,s= get_question_data()

    #get question for graphical version
    if graphical:
        return get_question_data()
    
    try:
        flush_input()
        answer = inputimeout(prompt="please, answer the question: {} + {} = ?".format(a,b),timeout=10)
    except TimeoutOccurred:
        return  False
    if str(s) == answer.replace(" ",""): return True

    return False
