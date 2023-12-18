import IDF
import VanillaFunctions as Vanilla

folder = "cleaned"


def CleanSentence(sentence, characters_to_erase=[',', '?', '!', '.', '-']):
    sentence = Vanilla.Lower(sentence)

    for char in characters_to_erase:
        sentence = sentence.split(char)
        sentence = " ".join(sentence)
    return [j for j in (sentence.split(" ")) if j != ""]






def SentenceTFIDF(sentence):                                                #Retourne l'ensemble des mots du corpus et la matrice TFIDF de la phrase sentence
    sentence = CleanSentence(sentence)
    tfidf = {}
    idf_dict = IDF.IDF(folder)
    for word in (idf_dict.keys()):
        if word in sentence:
            tfidf[word] = ((Vanilla.CountListe(sentence, word)/len(sentence))*idf_dict[word])
        else:
            tfidf[word] = 0
    return tfidf