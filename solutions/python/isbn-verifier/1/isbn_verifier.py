import string
def is_valid(isbn):
    isbn = ''.join(ch for ch in isbn if ch not in string.punctuation)
    total = 0
    for index in range(1,11):
        if len(isbn)!=10:
            return False
        elif isbn[-index] == 'X':
            if index !=1:
                return False
            total+=10*index
        elif isbn[-index].isdigit():
            total+=int(isbn[-index])*index
        else:
            return False
    return total%11==0
        
