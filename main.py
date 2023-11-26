from createFolder import *
from extractNames import *
from getTextFileName import *
from presidentsSpeeches import *

from TF import *
from IDF import *
from mostImportantWord import *
from leastImportantWors import *
from FinalScoreDict import *

basefolder = "speeches"
cleanfolder = "cleaned"

presidents_surnames = extractNames(basefolder, "txt")
print(presidents_surnames)

presidents_names_lastname = []
for name in presidents_surnames:
    presidents_names_lastname.append((associateName(name), name))
print(presidents_names_lastname)

presidents_speeches = presidentsSpeeches(presidents_surnames, basefolder)
print(presidents_speeches, sep='\n')

files = getTextFilesName(basefolder)

createFolder(cleanfolder)
createCleanedFiles(files, basefolder)
removePunctuation(cleanfolder)

print(LeastImportantWords(cleanfolder))
print(MostImportantWord(cleanfolder))



