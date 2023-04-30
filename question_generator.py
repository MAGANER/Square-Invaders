import random



__time_to_ask = 0
__time_to_answer = 0
def tick_qtime():
    global __time_to_ask
    __time_to_ask = __time_to_ask + 1
def tick_atime():
    global __time_to_answer
    __time_to_answer = __time_to_answer + 1
    
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
    if __time_to_answer < 25:
        answer = input("please, answer the question: {} + {} = ?".format(a,b))
        if str(s) == answer.replace(" ",""): return True

    return False
