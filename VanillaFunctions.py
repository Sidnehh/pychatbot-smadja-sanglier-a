def Sorted(liste): #bogo sort
    numbers_list = []
    str_list = []
    for l in liste:
        if str(l) == l:
            str_list.append(l)
        else:
            numbers_list.append(l)

def Lower(word):
    lower_word = ""
    for a in word:
        letter = a
        if ord('A') <= ord(letter) <= ord('Z'):
            letter = chr(ord(letter)+32)
        lower_word += letter
    return lower_word

def CountStr(liste, elmt):
    return int((len(liste)-len("".join(liste.split(elmt))))/len(elmt))
def CountListe(liste, elmt):
    c = 0
    for el in liste:
        if el == elmt:
            c+=1
    return c