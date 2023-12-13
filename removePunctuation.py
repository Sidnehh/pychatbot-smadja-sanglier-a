from getTextFilesName import *

punctuation_to_space = [ '"','#','$','%','&',"'",')','*','+','-','/']
punctuation_to_delete = ['.',',','!','?']
def removePunctuation(cleanedfolder):                   # Retire la ponctuation de tous les fichiers d'un dossier
    cleaned_files = getTextFilesName(cleanedfolder)     # cleanedfolder
    for file in cleaned_files:
        cleanedpath = cleanedfolder + "/" + file
        with open(cleanedpath, "r") as clean:
            lines = clean.readlines()

            for line in range(len(lines)):
                for symbol in punctuation_to_space:
                    lines[line] = " ".join(lines[line].split(symbol))
                for symbol in punctuation_to_delete:
                    lines[line] = "".join(lines[line].split(symbol))
            with open(cleanedpath, "w") as clean:
                clean.writelines(lines)