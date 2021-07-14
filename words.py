import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word = open("words.txt","r")
    file_data = word.read()
    word_list = file_data.split()
    return word_list
load_words()

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word