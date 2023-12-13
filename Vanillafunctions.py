def Max(list):
    maximum = list[0]
    for elt in list:
        if elt > maximum:
            maximum = elt
    return maximum
def Min(list):
    maximum = list[0]
    for elt in list:
        if elt < maximum:
            maximum = elt
    return maximum
def Sort(list):
    sorted_list = []
    while len(list) > 0:
        idmini = 0
        for i in range(len(list)):
            if str(list[i]) < str(list[idmini]):
                idmini = i
        sorted_list.append(list[idmini])
        del list[idmini]
    return sorted_list

def Lower(stringchain):
    ch = ""
    for letter in stringchain:
        if ord('A') <= ord(letter) <= ord('Z'):
            ch += chr(ord(letter)+32)
        else:
            ch += letter
    return ch
def Sum(list):
    somme = 0
    for elt in list:
        somme += elt
    return somme