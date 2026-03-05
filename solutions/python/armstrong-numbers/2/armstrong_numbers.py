def is_armstrong_number(number):
    digits = []
    original = number
    while number:
        digits.append(number%10)
        number //= 10
    power = len(digits)
    return original == sum(digits[i]**power for i in range(power))
    
        
