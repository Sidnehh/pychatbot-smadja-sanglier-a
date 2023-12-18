IMPORTS_AUTHORIZED = False
PREDEFINED_FUNCTIONS_AUTHORIZED = True

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

    return_matrix = [[0 for y in range(len(idf_dict))] for x in range(len(files))]

    words = list(idf_dict.keys())

    if PREDEFINED_FUNCTIONS_AUTHORIZED:
        words = sorted(words)

    for file_id in range(len(files)):
        tf_dict = TF(files[file_id], folder)
        for word_id in range(len(words)):
            return_matrix[file_id][word_id] = round(FinalScoreDict(idf_dict, tf_dict, words[word_id]), 4)



    return [files, words]+TransposeMatrix(return_matrix)

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
        mat = generate_TFIDF_matrix(folder)
        for file in mat:
            print(file)




