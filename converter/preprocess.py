"""
Converting the Abusive Speech to Normal Speech
""" 

import re

# Hate removal setup
hate_re = re.compile("fuck up|fuck off|piss off|fucked up|jack asses")
lexicon = open("converter/processedlexicon.dat").readlines()
lexicon = set([x.strip() for x in lexicon] + 
              [x.strip()+"ing" for x in lexicon] + 
              [x.strip()+"in" for x in lexicon])


def preprocess (sentence):
    cleaned = clean_english (sentence)
    return remove_hate (cleaned)


def clean_english (sentence):
    """
    Clean the english
    """

    if (len (sentence) < 2):
        sentence = "Please enter longer sentence ."

    sentence = sentence.lower()

    def decontracted(phrase):
        # specific
        phrase = re.sub(r"won\'t", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        return phrase

    # Joing contractions
    contractions = ["'ll", "'t", "'ve", "'s", "'d", "'re", "'m"]
    for c in contractions:
        sentence = re.sub(" " + c + " ", c + " ", sentence)
        
    # Remove useless apostrophes
    sentence = re.sub(r"""["?$!]|'(?!(?<! ')[lvdrtsm])""", "", sentence)

    sentence = decontracted(sentence)
    # print (sentence)
    return sentence


def remove_hate(sent):
    sent = re.sub(hate_re,"",sent.strip())
    sent= re.sub(" +"," ",sent)
    sent = sent.split(" ")
    sent = [word for word in sent if word not in lexicon]
    sentence = " ".join(sent)
    # print (sentence)
    return sentence

