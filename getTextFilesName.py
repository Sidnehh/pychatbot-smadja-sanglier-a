import os
presidentsNames = {"Chirac": "Jacques", "Giscard dEstaing": "Valérie", "Hollande": "François", "Macron": "Emmanuel",
                   "Mitterrand": "François", "Sarkozy": "Nicolas"}
presidentsMandates = {"Chirac": (1995, 2007), "Giscard dEstaing": (1974, 1981), "Hollande": (2012, 2017), "Macron": (2017, 2023),
                   "Mitterrand": (1981, 1995), "Sarkozy": (2007, 2012)}
def getTextFilesName(folder, extension="txt"):  # Retourne une liste des noms des fichiers
    files_name = []                             # contenus dans un dossier folder.
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            files_name.append(filename)
    return files_name

def associateName(lastname):            # Associe un prénom à un nom de président.
    return presidentsNames[lastname]

def associateFilesToName(file):                 # Associe un nom de président à un fichier texte
    name = file[len("Nomination_"):-len(".txt")]
    if '9'>=name[-1]>='0':
        name = name[:-1]
    return name