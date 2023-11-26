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

basefolder = "speeches"
cleanfolder = "cleaned"

presidents_surnames = extractNames(basefolder, "txt")
print("Noms des présidents : ", presidents_surnames)

presidents_names_lastname = []
for name in presidents_surnames:
    presidents_names_lastname.append((associateName(name), name))
print("Noms et prénoms des présidents : ", presidents_names_lastname)

presidents_speeches = presidentsSpeeches(presidents_surnames, basefolder)
print("Correspondance présidents-discours : ", presidents_speeches)

files = getTextFilesName(basefolder)

createFolder(cleanfolder)
createCleanedFiles(files, basefolder)
removePunctuation(cleanfolder)

print("Mots les moins importants : ", LeastImportantWords(cleanfolder)) # la valeur de séparation (0) peut être changée
print("Mot le plus important : ", MostImportantWord(cleanfolder))



