from createFolder import *
from extractNames import *
from getTextFilesName import *
from createCleanedFiles import *
from presidentsSpeeches import *

from TF import *
from IDF import *
from MostImportantWord import *
from LeastImportantWords import *

from removePunctuation import *
from FinalScoreDict import *

from TFIDFMAT import generate_TFIDF_matrix, PrintCleanMatrix
least_important = 1
most_important = 2
most_repeated = 3
who_talked_about_word = 4
who_repeated_it_the_most = 5
who_said_it_first = 6
they_all_said_it = 7

basefolder = "speeches"
cleanfolder = "cleaned"

folder = "cleaned"

presidents_surnames = extractNames(basefolder, "txt")
presidents_names_lastname = []

for name in presidents_surnames:
    presidents_names_lastname.append((associateName(name), name))

presidents_speeches = presidentsSpeeches(presidents_surnames, basefolder)
files = getTextFilesName(basefolder)
createFolder(cleanfolder)
createCleanedFiles(files, basefolder)
removePunctuation(cleanfolder)

def TakeInput(user_input):
    match user_input:
        case 1:
            print("Mots les moins importants : ", LeastImportantWords(cleanfolder))
        case 2:
            print("Mot le plus important : ", MostImportantWord(cleanfolder))
        case 3:
            print(MostRepeatedWord(cleanfolder))
        case 4:
            word = input("Saisissez un mot à rechercher : ")
            files = getTextFilesName(cleanfolder)
            presidents_who_talked = set({})
            for file in files:
                #print(TF(file, cleanfolder).keys())
                if word in TF(file, cleanfolder).keys():
                    presidents_who_talked = {associateFilesToName(file)} | presidents_who_talked
            print("Les présidents qui ont parlé de", word, ": ", presidents_who_talked)


        case 5:
            word = input("Saisissez un mot à rechercher : ")
            tfs = []
            files = getTextFilesName(cleanfolder)
            maxval = 0
            president = "inexistant"
            for file in files:
                tf = TF(file, folder)
                if word in tf.keys():
                    if tf[word]>maxval:
                        president = associateFilesToName(file)
                        maxval = tf[word]
            print("Le président qui a répété le plus le mot '", word, "' est", president)


        case 6:
            word = input("Saisissez un mot à rechercher : ")
            files = getTextFilesName(folder)

            president = "inexistant"

            minval = 2023
            for file in files:
                tf = TF(file, folder)
                if word in tf.keys():
                    if presidentsMandates[associateFilesToName(file)][0]<minval:
                        president = associateFilesToName(file)
                        minval = presidentsMandates[associateFilesToName(file)][0]

            print("Le président qui a dit le mot '", word, "' en premier est", president)


        case 7:
            words = []
            filteredwords = set(IDF(folder).keys())
            files = getTextFilesName(folder)
            for file in files:
                tf = TF(file, folder)
                tfwords = set(tf.keys())
                filteredwords &= tfwords
            filteredwords = list(filteredwords)
            print("Les mots que tous les présidents ont dits sont ", filteredwords)
        case 8:
            print(PrintCleanMatrix(generate_TFIDF_matrix(folder)))
