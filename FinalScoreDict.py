def FinalScoreDict(IDF_, TF_, word):                    # Retourne la valeur du vecteur TF-IDF d'une chaîne de caractères
    if word not in TF_.keys():                          # word
        return 0
    else:
        return (TF_[word]) * (IDF_[word])
