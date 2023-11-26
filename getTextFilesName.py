import os
presidentsNames = {"Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François", "Macron": "Emmanuel",
                   "Mitterrand": "François", "Sarkozy": "Nicolas"}
def getTextFilesName(folder, extension="txt"):  # Retourne une liste des noms des fichiers
    files_name = []                             # contenus dans un dossier folder.
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            files_name.append(filename)
    return files_name

def associateName(lastname):            # Associe un prénom à un nom de président.
    return presidentsNames[lastname]