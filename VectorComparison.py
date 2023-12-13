import math

from SentenceTFIDF import SentenceTFIDF
from TFIDFMAT import generate_TFIDF_matrix, TransposeMatrix

from getTextFilesName import getTextFilesName
def VectorsCosine(vec1, vec2):
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

def DocumentWithMostSimilarity(sentence, folder):
    sentence = SentenceTFIDF(sentence)
    tfidf_matrix = TransposeMatrix(generate_TFIDF_matrix(folder))
    print(tfidf_matrix[1:])

    highest_similarity = 0
    files = getTextFilesName(folder)
    wantedfile = 0
    file_id = 0


    for file in tfidf_matrix[1:]:
        if VectorsCosine(sentence[1], file)>highest_similarity:
            highest_similarity = VectorsCosine(sentence[1], file)
            wantedfile = file_id
        file_id+=1
    return files[wantedfile]

print(DocumentWithMostSimilarity("Bonjour mes chers con citoyens", "cleaned"))