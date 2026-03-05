def is_armstrong_number(number):
    count = 0 
    digits = []
    original = number
    while number:
        digits.append(number%10)
        number //= 10
        count+=1
    return original == sum(digits[i]**count for i in range(count))
    
        
