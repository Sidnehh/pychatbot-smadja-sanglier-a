from TF import TF
from IDF import IDF
from getTextFilesName import getTextFilesName


def generate_TFIDF_matrix(folder):
    files = getTextFilesName(folder)
    mat = []
    for file in files:


