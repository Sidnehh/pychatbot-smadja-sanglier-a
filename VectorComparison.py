import math

from SentenceTFIDF import SentenceTFIDF
from TFIDFMAT import generate_TFIDF_matrix, TransposeMatrix
from getTextFilesName import getTextFilesName

def VectorsCosine(vec1, vec2): #pas utile mais peut l'être si l'on change la façon dont la similarité est générée
    sum = 0
    if len(vec1)<len(vec2):
        vec1 += [0 for i in range(len(vec2)-len(vec1))]
    elif len(vec2)<len(vec1):
        vec2 += [0 for i in range(len(vec1)-len(vec2))]

    for i in range(len(vec1)):
        sum+=vec1[i]*vec2[i]

    s1 = 0
    s2 = 0
    for i in range(len(vec1)):
        s1 += vec1[i]**2
        s2 += vec2[i]**2
    s1 = math.sqrt(s1)
    s2 = math.sqrt(s2)

    return sum/(s1+s2)

def DictsCosine(vec1, vec2):
    sum = 0
    if len(vec1)!=len(vec2):
        return "Abort : cannot compute cosine of dictionaries with different sizes"
    if set(vec1.keys()) != set(vec2.keys()):
        return "Abort : cannot compute cosine of dictionaries with different keys"

    for word in vec1.keys():
        sum+=vec1[word]*vec2[word]
    s1 = 0
    s2 = 0
    for word in vec1.keys():
        s1 += vec1[word]**2
        s2 += vec2[word]**2
    s1 = math.sqrt(s1)
    s2 = math.sqrt(s2)

    return sum/(s1+s2)

def DocumentWithMostSimilarity(sentence, folder):
    sentencetfidf = SentenceTFIDF(sentence)
    tfidf_matrix = generate_TFIDF_matrix(folder)
    words = tfidf_matrix[1]
    tfidf_matrix = TransposeMatrix(tfidf_matrix)

    highest_similarity = 0
    files = getTextFilesName(folder)
    wantedfile = 0
    file_id = 0

    for file in tfidf_matrix:
        file = file[2:]
        filedict = {words[word]:file[word] for word in range(len(words))}
        value = DictsCosine(sentencetfidf, filedict)
        if value>highest_similarity:
            highest_similarity = value
            wantedfile = file_id
        file_id+=1
    return files[wantedfile]
