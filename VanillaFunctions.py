def Sorted(liste): #bogo sort
    pass
def Enumerate(liste):
    pass
def Lower(word):
    lower_word = ""
    for a in word:
        letter = a
        if ord('A') <= ord(letter) <= ord('Z'):
            letter = chr(ord(letter)+32)
        lower_word += letter
    return lower_word
