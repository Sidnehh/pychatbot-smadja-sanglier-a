from getTextFilesName import *
from FinalScoreDict import *
from IDF import *
from TF import *
def MostImportantWord(folder):
    folder = folder + "/"

    value_to_discard = 0

    files = getTextFilesName(folder)

    max_word = ""

    idf_dict_init = IDF(folder)
    idf_dict = IDF(folder)
    for file in files:
        tf_dict = TF(file, folder)
        for word in tf_dict.keys():
            word = str(word)
            if FinalScoreDict(idf_dict, tf_dict, word) > FinalScoreDict(idf_dict, tf_dict, max_word):
                max_word = word
    return max_word
