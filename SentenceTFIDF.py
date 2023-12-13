import IDF

folder = "cleaned"


def CleanSentence(sentence, characters_to_erase=[',', '?', '!', '.', ':', "'"]):
    sentence = sentence.lower()

    for char in characters_to_erase:
        sentence = sentence.split(char)
        sentence = " ".join(sentence)
    return [j for i, j in enumerate(sentence.split(" ")) if j != ""]


def IntersectingWords(words):                           #Renvoie une liste des mots qui sont à la fois dans la liste word, et dans la matrice TFIDF
    words = OrderedSet(words)
    idf_set = IDF.IDF(folder).keys()
    return [word for word in words if word in idf_set]

def OrderedSet(lst):
    lst_set = set(lst)
    ordered_set = []
    for elt in lst:
        if elt not in ordered_set:
            ordered_set.append(elt)
    return ordered_set
def SentenceTFIDF(sentence):
    sentence = CleanSentence(sentence)
    sentence_set = OrderedSet(sentence)
    tfs = []
    idf_dict = IDF.IDF(folder)
    for word in sorted(idf_dict.keys()):
        if word in sentence:
            tfs.append((sentence.count(word)/len(sentence))*idf_dict[word])
        else:
            tfs.append(0)
    return [sorted(idf_dict.keys()), tfs]


print(SentenceTFIDF("Coucou ça va ? Je vais bien et toi bisous."))
