import os
def createFolder(folder):  # Crée un dossier dans le répertoire actuel, ayant pour nom l'argument folder.
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print("Error creating directory : ", folder)
