import math 

def score(x, y):
    distance = math.hypot(x,y) 
    if distance>10:
        return 0
    if distance>5:
        return 1
    if distance>1:
        return 5
    return 10