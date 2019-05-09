"""
Converting the Abusive Speech to Normal Speech
""" 

import re
from . import translate as tr
from . import preprocess as pp


def convert (sentence, mode='fr'):
    """
    Remove the hate and convert to non-offensive sentence
    """

    processed_sentence = pp.preprocess(sentence)
    if (len (processed_sentence) < 2):
        processed_sentence = "Please enter longer sentence ."
    return tr.translate (processed_sentence, target=mode)
