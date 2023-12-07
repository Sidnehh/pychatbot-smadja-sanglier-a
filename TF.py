chardet_present = True
try:
    import chardet
except:
    chardet_present = False


def TF(file, folder=''):                                    # Partie TF :
    folder = folder + "/"                                   # Retourne un dictionnaire associant chaque mot d'un fichier
    words_count = {}                                        # à une fréquence d'apparition dans le texte du fichier.
    encodingInfo = {}
    with open(folder+file, 'rb') as f:
        try:
            encodingInfo = chardet.detect(f.read())
        except:
            if not chardet_present:
                if "Chirac2" in file:
                    encodingInfo['encoding'] = 'windows-1252'
                else:
                    encodingInfo['encoding'] = 'utf-8'
    with (open(folder+file,'r', encoding = encodingInfo['encoding']) as f):
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
if __name__=="__main__":
    print(TF("Nomination_Chirac2.txt", "cleaned"))