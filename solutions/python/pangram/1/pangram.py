import string
def is_pangram(sentence):
    sentence = sentence.upper()
    return set(string.ascii_uppercase)<= set(sentence)
