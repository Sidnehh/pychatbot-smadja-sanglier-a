def removePunctuation(cleanedfolder):                   #cette fonction ne marche pas, mais elle est censée
    cleaned_files = getTextFilesName(cleanedfolder)     #retirer la ponctuation de tous les fichiers d'un
    for file in cleaned_files:                          #dossier folder.
        cleanedpath = cleanedfolder + "/" + file
        with open(cleanedpath, "r") as clean:
            lines = clean.readlines()

            #for line in range(len(lines)):
            #    for character in range(len(line)):
            #        if lines[line][character] in punctuation:
            for line in range(len(lines)):
                for symbol in punctuation_to_space:
                    lines[line] = " ".join(lines[line].split(symbol))
            with open(cleanedpath, "w") as clean:
                clean.writelines(lines)
