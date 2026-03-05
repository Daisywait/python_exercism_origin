"""Classify numbers as perfect, abundant, or deficient."""
from math import sqrt
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot_sum = 1
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    for i in range(2,int(sqrt(number))+1):
        if number%i==0:
            aliquot_sum+=i
            j = number//i
            if j!=i:
                aliquot_sum+=j
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"