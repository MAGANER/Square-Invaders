import random
from inputimeout import inputimeout, TimeoutOccurred


__time_to_ask = 0
def tick_qtime():
    global __time_to_ask
    __time_to_ask = __time_to_ask + 1
    
def can_ask():
    global __time_to_ask
    if __time_to_ask > 30:
        __time_to_ask = 0
        return True
    return False

def ask():
    a = random.randint(1,100)
    b = random.randint(1,100)
    s = a+b
    try:
        answer = inputimeout(prompt="please, answer the question: {} + {} = ?".format(a,b),timeout=10)
    except TimeoutOccurred:
        return  False
    if str(s) == answer.replace(" ",""): return True

    return False
