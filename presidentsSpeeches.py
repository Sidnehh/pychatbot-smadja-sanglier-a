from getTextFilesName import *
def presidentsSpeeches(presidents, folder):
    president_speeches = {}
    for president in presidents:
        for file in getTextFilesName(folder):
            if president in file:
                if(president in president_speeches.keys()):
                    president_speeches[president].append(file)
                else:
                    president_speeches[president] = [file]

    return president_speeches
