import IDF
from Vanillafunctions import Lower
from Vanillafunctions import Sort

folder = "cleaned"


def CleanSentence(sentence, characters_to_erase=[',', '?', '!', '.', ':', "'"]): #Convertit une phrase sentence en liste de mots sans ponctuation.
    sentence = Lower(sentence)

    for char in characters_to_erase:
        sentence = sentence.split(char)
        sentence = " ".join(sentence)
    sentence = sentence.split(" ")
    return [sentence[j] for j in range(len(sentence)) if sentence[j] != ""]


def IntersectingWords(words):                           #Renvoie une liste des mots qui sont à la fois dans la liste word, et dans la matrice TFIDF
    words = OrderedSet(words)
    idf_set = IDF.IDF(folder).keys()
    return [word for word in words if word in idf_set]

def OrderedSet(lst):        #Renvoie un set ordonné d'une liste lst
    lst_set = Sort(list(set(lst)))
    return lst_set
def SentenceTFIDF(sentence):
    sentence = CleanSentence(sentence)
    sentence_set = set(sentence)
    tfs = []
    idf_dict = IDF.IDF(folder)
    for word in sorted(idf_dict.keys()):
        if word in sentence:
            tfs.append((sentence.count(word)/len(sentence))*idf_dict[word])
        else:
            tfs.append(0)
    return [sorted(idf_dict.keys()), tfs]


print(CleanSentence("Coucou, je m'appelle Sidney."))
