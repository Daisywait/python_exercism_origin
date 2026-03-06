def is_valid(isbn):
    isbn = isbn.replace('-','')
    total = 0
    if len(isbn) != 10:
        return False
        
    for index in range(1,11):
        ch = isbn[-index]
        if ch == 'X':
            if index !=1:
                return False
            total+=10*index
        elif ch.isdigit():
            total+=int(ch)*index
        else:
            return False
    
    return total%11==0
        
