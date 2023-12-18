


def TF(file, folder=''):                                    # Partie TF :
    folder = folder + "/"                                   # Retourne un dictionnaire associant chaque mot d'un fichier
    words_count = {}                                        # à une fréquence d'apparition dans le texte du fichier.
    encodingInfo = {}
    with (open(folder+file,'r', encoding = 'utf-8') as f):
        lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].replace('\n', '').split(" ")
            for word in line:
                if word != '\n':
                    if word not in words_count.keys():
                        words_count[word] = 1
                    else:
                        words_count[word] += 1
    mysum = sum(words_count.values())
    for key in words_count.keys():
        words_count[key] /= mysum
    return words_count
