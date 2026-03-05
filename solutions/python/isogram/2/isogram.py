def is_isogram(text):
    clean_string = ''.join(s for s in text if s.isalpha())
    return len(clean_string) == len(set(clean_string.lower()))
