from VectorComparison import *
from SentenceTFIDF import *
from TFIDFMAT import *
from VanillaFunctions import *
from IDF import *

endingpunctuation = ['.', '!', '-']
question_starters = {'comment':'Après analyse, ' , 'pourquoi':'Car ', 'peux-tu': 'Oui, bien sûr ! ', 'quels': 'Ceux-ci : ', 'quel':"Il s'agit de, "}

def MaxTFIDFQuestion(question):
    question_TFIDF = SentenceTFIDF(question)
    idmaxscore = list(question_TFIDF.keys())[0]
    for word in question_TFIDF.keys():
        if question_TFIDF[word] > question_TFIDF[idmaxscore]:
            idmaxscore = word
    return idmaxscore


def WordInDocuments(word, folder): #vérifie si un mot est contenu dans l'ensemble du corpus. Par exemple si
    allwords = "".join(IDF(folder).keys()) #on cherche le mot "climat", et qu'on a "climatique", on retournera True
    return word in allwords


def FirstOccurenceSentence(word, file, folder = "speeches"):
    word = Lower(word)
    with open(folder+'/'+file, 'r', encoding = 'utf-8') as f:
        lines = Lower(''.join(f.readlines()))
    lines = lines.split('\n')
    lines = " ".join(lines)
    lines = lines.split('- ')
    lines = ''.join(lines)
    lines = lines.split(' -')
    lines = ''.join(lines)
    lines = lines.split('.')

    for sentence in lines:
        if word in sentence:
            return sentence

def SentenceWithHighestSimilarity(question, file, folder="speeches"):
    with open(folder+'/'+file, 'r', encoding = 'utf-8') as f:
        lines = Lower(''.join(f.readlines()))
    lines = lines.split('\n')
    lines = " ".join(lines)
    lines = lines.split('- ')
    lines = ''.join(lines)
    lines = lines.split(' -')
    lines = ''.join(lines)
    lines = lines.split('.')

    highest_sentence_id = 0
    highest_similarity = 0
    sentence_id = 0

    question_tfidf = SentenceTFIDF(question)

    for sentence in lines:
        if DictsCosine(SentenceTFIDF(sentence), question_tfidf) > highest_similarity:
            highest_similarity = DictsCosine(SentenceTFIDF(sentence), question_tfidf)
            highest_sentence_id = sentence_id
        sentence_id += 1
    return lines[highest_sentence_id]

def AnswerGenerator(question, foldr="speeches"):
    if question == "":
        return "Veuillez saisir une question. "
    id_quest = CleanSentence(question)[0]
    relevantword = MaxTFIDFQuestion(question)
    print("Mot avec le TFIDF le plus élevé :", relevantword)
    if relevantword == "":
        return "Pas d'information à ce sujet."
    answer = FirstOccurenceSentence(relevantword, DocumentWithMostSimilarity(question, folder))
    if answer == None:
        answer = SentenceWithHighestSimilarity(question, DocumentWithMostSimilarity(question, folder))
    print("Document avec le plus de similarités : ", DocumentWithMostSimilarity(question, folder))
    print(id_quest, answer)
    if id_quest in question_starters.keys():
        answer = question_starters[id_quest]+answer
    return answer



