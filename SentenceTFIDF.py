import IDF

folder = "cleaned"


def CleanSentence(sentence, characters_to_erase=[',', '?', '!', '.']):
    sentence = sentence.lower()

    for char in characters_to_erase:
        sentence = sentence.split(char)
        sentence = " ".join(sentence)
    return [j for i, j in enumerate(sentence.split(" ")) if j != ""]


def IntersectingWords(words):
    words = OrderedSet(words)
    idf_set = IDF.IDF(folder).keys()

    return [word for word in words if word in idf_set]

def OrderedSet(lst):
    lst_set = sorted(list(set(lst)))
    return lst_set

def SentenceTFIDF(sentence):                                                #Retourne l'ensemble des mots du corpus et la matrice TFIDF de la phrase sentence
    sentence = CleanSentence(sentence)
    sentence_set = OrderedSet(sentence)
    tfs = []
    idf_dict = IDF.IDF(folder)
    for word in sorted(idf_dict.keys()):
        if word in sentence_set:
            tfs.append((sentence.count(word)/len(sentence))*idf_dict[word])
        else:
            tfs.append(0)
    return [sorted(idf_dict.keys()), tfs]