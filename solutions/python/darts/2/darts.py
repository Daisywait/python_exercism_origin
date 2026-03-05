import math 

def score(x_coordinate, y_coordinate):
    distance = math.hypot(x_coordinate, y_coordinate) 
    if distance>10:
        return 0
    if distance>5:
        return 1
    if distance>1:
        return 5
    return 10