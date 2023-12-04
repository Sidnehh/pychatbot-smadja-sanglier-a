import magic

blob = open('unknown-file', 'rb').read()
m = magic.open(magic.MAGIC_MIME_ENCODING)
m.load()
encoding = m.buffer(blob)  # "utf-8" "us-ascii" etc


def TF(file, folder=''):                                    # Partie TF :
    folder = folder + "/"                                   # Retourne un dictionnaire associant chaque mot d'un fichier
    words_count = {}                                        # à une fréquence d'apparition dans le texte du fichier.
    with (open(folder+file,'rt', encoding = 'latin-1') as f):
        lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].split(" ")
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
    print(TF("Nomination_Chirac1.txt", "cleaned"))