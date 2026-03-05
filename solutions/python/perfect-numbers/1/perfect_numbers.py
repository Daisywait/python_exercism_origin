from math import sqrt
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = 0
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,int(sqrt(number)+1)):
        j = number//i
        if number%i == 0:
            if j!=1 and j!=number and j!=i:
                aliquot_sum= aliquot_sum + i + j
            elif i!=number:
                aliquot_sum+=i
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"