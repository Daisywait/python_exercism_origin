def triangle(f):
    def inner(sides):
        return sum(sides)>max(sides)*2 and f(sides)
    return inner

@triangle    
def equilateral(sides):
    return  len(set(sides))==1

@triangle    
def isosceles(sides):
    return  len(set(sides))< 3
    
@triangle    
def scalene(sides):
    return  len(set(sides))==3

    