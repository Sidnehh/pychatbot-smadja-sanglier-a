from getTextFilesName import *
from FinalScoreDict import *
from IDF import *
from TF import *
def LeastImportantWords(folder):                        # Retourne une liste des mots les moins importants du corpus
                                                        # folder (ceux dont le score TF-IDF = 0)
    folder = folder+"/"

    value_to_discard = 0

    files = getTextFilesName(folder)

    idf_dict_init = IDF(folder)
    idf_dict = IDF(folder)
    for file in files:
        tf_dict = TF(file, folder)
        for word in tf_dict.keys():
            word = str(word)
            if FinalScoreDict(idf_dict_init, tf_dict, word)!=value_to_discard:
                if word in idf_dict.keys():
                    del idf_dict[word]

    return sorted(idf_dict.keys())
