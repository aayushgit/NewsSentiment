# -*- coding: utf-8 -*-

from nltk.book import *
def lexical_diversity(text):
        return len(text)/len(set(text))

def percentage(count,total):
        return 100*count/total
    