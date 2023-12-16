IMPORTS_AUTHORIZED = False

from LeastImportantWords import *

from removePunctuation import *
from FinalScoreDict import *

if IMPORTS_AUTHORIZED:
    import numpy

def TransposeMatrix(mat1):
    mat2 = [[mat1[y][x] for y in range(len(mat1))] for x in range(len(mat1[0]))]
    return mat2

def generate_TFIDF_matrix(folder):
    files = getTextFilesName(folder)
    idf_dict = IDF(folder)
    nwords = len(idf_dict)
    filescores = [associateFilesToName(file) for file in files]

    return_matrix = [[0 for y in range(nwords)] for x in range(len(filescores)+1)]
    for word in range(nwords):
        return_matrix[0][word] = sorted(idf_dict.keys())[word]
    for file_id, file in enumerate(files):
        tf_dict = TF(file, folder)
        for word_id, word in enumerate(sorted(idf_dict.keys())):
            return_matrix[file_id+1][word_id] = round(FinalScoreDict(idf_dict, tf_dict, word), 4)



    return TransposeMatrix(return_matrix)

def PrintCleanMatrix(matrix):
    if IMPORTS_AUTHORIZED:
        import sys
        numpy.set_printoptions(threshold=sys.maxsize)
        print(numpy.array(matrix))
    else:
        for line in matrix:
            print(matrix)

if __name__ == '__main__':

    folder = "cleaned"
    print(getTextFilesName(folder))
    if IMPORTS_AUTHORIZED:
        import sys
        numpy.set_printoptions(threshold=sys.maxsize)
        print(numpy.array(generate_TFIDF_matrix(folder)))
    else:
        print(generate_TFIDF_matrix(folder))



