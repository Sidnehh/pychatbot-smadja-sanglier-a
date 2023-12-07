import math
from getTextFilesName import *
import operator

from TF import *

def IDF(folder, extension='txt'):                           # Partie IDF :
                                                            # Retourne un dictionnaire associant chaque mot présent dans
                                                            # le corpus folder à un score indiquant sa présence (+ le score
                                                            # est faible, + il apparaît)
    folder = folder + "/"
    allwords = {}                                           # Dictionnaire qui va associer chaque mot de chaque document à son indice IDF
    files = getTextFilesName(folder)
    tfs = []                                              #liste des dictionnaires TF pour chaque fichier


    for file in files:                                      # Crée un dictionnaire TF par fichier
        tf = TF(file, folder)                             #
        tfs.append(tf)                                  # Ajoute le dictionnaire TF à la liste "dicts"
        file_allwords = set(tf.keys())                    # Crée un set qui permet de supprimer les doublons de clés (mesure de sécurité)
        new_fileallwords = {key : 0 for key in file_allwords} #Crée un nouveau dictionnaire où chaque mot est associé à 0
        allwords = allwords|new_fileallwords                # Opération logique qui permet de joindre deux dictionnaires
                                                            # (étant donné que ce ne sont que des 0 ils seront écrasés ou conservés)
                                                            # (si un mot est déjà enregistré, cela permet de l'ignorer)

    for file in range(len(files)):                          # pour chaque mot enregistré dans les dictionnaires TF, on va ajouter 1 à leur équivalent dans "allwords"
        for key in tfs[file].keys():                      # cela permet de savoir dans combien de fichiers est contenu un mot
            allwords[key]+=1
    for key in allwords.keys():                             # on effectue l'opération idf pour chaque mot
        allwords[key] = math.log((float(len(tfs))/(float(allwords[key]))), 10.0)
    return allwords

def MostRepeatedWord(folder, extension='txt'): # trouve le mot le plus répété du dossier



    folder = folder + "/"
    allwords = {}
    files = getTextFilesName(folder)
    tfs = []


    for file in files:
        tf = TF(file, folder)
        tfs.append(tf)
        file_allwords = set(tf.keys())
        new_fileallwords = {key : 0 for key in file_allwords}
        allwords = allwords|new_fileallwords



    for file in range(len(files)):
        for key in tfs[file].keys():
            allwords[key]+=tfs[file][key] * sum(tfs[file].values())

    return max(allwords, key=allwords.get)
