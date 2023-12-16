from VectorComparison import *
from SentenceTFIDF import *
from TFIDFMAT import *
import VanillaFunctions as v
from IDF import *

endingpunctuation = ['.', '!', '-']
question_starters = {'comment':'Après analyse, ' , 'pourquoi':'Car ', 'peux-tu': 'Oui, bien sûr ! ', 'quels': 'Ceux-ci : ', 'quel':"Il s'agit de, "}

def MaxTFIDFQuestion(question):
    question_TFIDF = SentenceTFIDF(question)
    idmaxscore = 0
    for i in range(len(question_TFIDF[0])):
        if question_TFIDF[1][i] > question_TFIDF[1][idmaxscore]:
            idmaxscore = i
    return question_TFIDF[0][idmaxscore]

def DocToWords(document):
    path = "speeches/"+document
    f = open(path, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()
    lst_words = []
    for i in range(len(content)):
        words = content[i][:-1].split(' ')
        for word in words:
            lst_words.append(word)
    return lst_words

def WordInDocuments(word, folder):
    allwords = list(IDF(folder).keys())
    for a in allwords:
        if word in a:
            return True
    return False

def FirstOccurenceSentence(word, file):
    file_words = DocToWords(file)
    id = 0
    while (v.Lower(word) not in v.Lower(file_words[id])) and id+1 < len(file_words):
        id += 1
    id_occurence = id

    idend = id_occurence
    while ('.' not in file_words[idend]) and ('-' and '!' and '?' != file_words[idend]) and (idend+1 < len(file_words)):
        idend+=1
    idend += 1

    idstart = id_occurence-1
    while ('.' not in file_words[idstart]) and ('-' and '!' and '?' != file_words[idstart]) and idstart > 0:
        idstart-=1
    idstart += 1

    sentence = ""
    for i in range(idstart, idend):
        sentence += file_words[i] + ' '
    if sentence[-1] != '.':
        sentence = sentence[:-1]+'.'

    return v.Lower(sentence)

def AnswerGenerator(question, folder="speeches"):
    if question == "":
        return "Veuillez saisir une question. "
    relevantword = MaxTFIDFQuestion(question)
    idquest = CleanSentence(question)[0]
    if relevantword == "":
        return "Pas d'information à ce sujet."
    answer = FirstOccurenceSentence(relevantword,DocumentWithMostSimilarity(question, folder))
    if idquest in question_starters.keys():
        answer = question_starters[idquest]+answer
    return answer



