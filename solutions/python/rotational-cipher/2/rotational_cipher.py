def rotate(text, key):
    upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters='abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for letter in text:
        if letter in upper_letters:
            letters = upper_letters
        elif letter in lower_letters:
            letters = lower_letters
        else:
            cipher+=letter
            continue
        cipher+=letters[(letters.index(letter)+key)%len(letters)]
    return cipher
            
