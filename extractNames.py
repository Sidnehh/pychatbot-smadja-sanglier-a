def extractNames(folder, extension="txt"):            # Retourne une de tous les noms des présidents
    files_name = getTextFilesName(folder, extension)  # extraits depuis un fichier folder.
    presidents = []
    for i in range(len(files_name)):
        name = files_name[i]
        name = name[len("Nomination_"):-(len(extension)+1)]
        if '0' <= name[-1] <= '9':
            name = name[:-1]
        if name not in presidents:
            presidents.append(name)

    return presidents
