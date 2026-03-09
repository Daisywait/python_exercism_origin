def rotate(text, key):
    upper_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters='abcdefghijklmnopqrstuvwxyz'
    Cipher = ''
    for letter in text:
        if letter in upper_letters:
            Cipher+=upper_letters[(upper_letters.index(letter)+key)%len(upper_letters)]
        elif letter in lower_letters:
            Cipher+= lower_letters[(lower_letters.index(letter)+key)%len(lower_letters)]
        else:
            Cipher+=letter
    return Cipher
            
