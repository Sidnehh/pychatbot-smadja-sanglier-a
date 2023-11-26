def createCleanedFiles(files, basefolder):              # Crée le dossier "cleaned" et y place des copies
    cleanedfolder = createCleanedDirectory()            # des fichiers files, avec son contenu en minuscules.
    for file in files:
        basepath = basefolder+"/"+file
        with open(basepath, 'r') as base:
            lines = base.readlines()
            for line in range(len(lines)):
                lines[line] = list(lines[line])
                for character in range(len(lines[line])):
                    if 'A'<=lines[line][character]<='Z':
                        lines[line][character] = chr(ord(lines[line][character])-(ord('A')-ord('a')))
                lines[line] = ''.join(lines[line])
            cleanedpath = "" + cleanedfolder + "/"+file
            with open(cleanedpath, 'w+') as clean:
                for line in lines:
                    clean.write(line)
