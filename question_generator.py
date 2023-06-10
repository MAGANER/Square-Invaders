import random
from inputimeout import inputimeout, TimeoutOccurred

def flush_input():
    try:
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
    
def can_ask():
    global __time_to_ask
    if __time_to_ask > 150:
        __time_to_ask = 0
        return True
    return False

def ask():
    a = random.randint(1,100)
    b = random.randint(1,100)
    s = a+b
    try:
        flush_input()
        answer = inputimeout(prompt="please, answer the question: {} + {} = ?".format(a,b),timeout=10)
    except TimeoutOccurred:
        return  False
    if str(s) == answer.replace(" ",""): return True

    return False
