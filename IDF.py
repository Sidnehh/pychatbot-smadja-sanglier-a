import math
from BaseFunctions import *
import operator

def IDF(folder, extension='txt'):                           # Partie IDF :
                                                            # Retourne un dictionnaire associant chaque mot présent dans
                                                            # le corpus folder à un score indiquant sa présence (+ le score
                                                            # est faible, + il apparaît)
    folder = folder + "/"
    allwords = {}                                           # Dictionnaire qui va associer chaque mot de chaque document à son indice IDF
    files = getTextFilesName(folder)
    dicts = []                                              #liste des dictionnaires TF pour chaque fichier


    for file in files:                                      # Crée un dictionnaire TF par fichier
        dict = TF(file, folder)                             #
        dicts.append(dict)                                  # Ajoute le dictionnai TF à la liste "dicts"
        file_allwords = set(dict.keys())                    # Crée un set qui permet de supprimer les doublons de clés (mesure de sécurité)
        new_fileallwords = {key : 0 for key in file_allwords} #Crée un nouveau dictionnaire où chaque mot est associé à 0
        allwords = allwords|new_fileallwords                # Opération logique qui permet de joindre deux dictionnaires
                                                            # (étant donné que ce ne sont que des 0 ils seront écrasés ou conservés)
                                                            # (si un mot est déjà enregistré, cela permet de l'ignorer)

    for file in range(len(files)):                          # pour chaque mot enregistré dans les dictionnaires TF, on va ajouter 1 à leur équivalent dans "allwords"
        for key in dicts[file].keys():                      # cela permet de savoir dans combien de fichiers est contenu un mot
            allwords[key]+=1
    for key in allwords.keys():                             # on effectue l'opération idf pour chaque mot
        allwords[key] = math.log((1.0/(allwords[key]/len(dicts)))+1, math.e)
    return allwords
