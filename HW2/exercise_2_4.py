import math
import random

def roll_dice(size, count):
    i = 0
    while i < count:
        print random.randint(1,size)
        i = i + 1

roll_dice(20,10)