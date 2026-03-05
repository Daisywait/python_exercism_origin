def triangle(sides):
    a,b,c = sides
    if a and b and c:
        return a+b>=c and a+c>=b and b+c>=a
    return False
def equilateral(sides):
    a,b,c = sides
    if triangle(sides):
        return a == b == c
    return False

def isosceles(sides):
    a,b,c = sides
    if triangle(sides):
        return a==b or a==c or b==c
    return False
    

def scalene(sides):
    a,b,c = sides
    if triangle(sides):
        return a!=b and a!=c and b!=c
    return False
    