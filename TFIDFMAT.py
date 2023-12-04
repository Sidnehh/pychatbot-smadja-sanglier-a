from TF import TF
from IDF import IDF
from getTextFilesName import getTextFilesName
from FinalScoreDict import FinalScoreDict

def generate_TFIDF_matrix(folder):
    files = getTextFilesName(folder)
    mat = []
    nwords = len(IDF(folder))
    for i in range(nwords):
        filescores = []
        for file in files:
            filescores.append(FinalScoreDict(TF(file, folder), IDF(folder), nwords[i]))
        mat.append(filescores)
    return mat



