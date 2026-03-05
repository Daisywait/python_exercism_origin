def response(hey_bob):
    hey_bob_clean = hey_bob.strip()
    if hey_bob_clean.endswith("?") and hey_bob_clean.isupper():
        return "Calm down, I know what I'm doing!" 
    if hey_bob_clean.endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if not hey_bob_clean:
        return "Fine. Be that way!"
    return "Whatever."