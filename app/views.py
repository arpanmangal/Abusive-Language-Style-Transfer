from flask import request, jsonify
from flask import current_app as app
import json, os
import random
import converter.convert as conv
from hatesonar import Sonar
from nltk.stem import PorterStemmer

PATH = os.path.dirname(os.path.abspath(__file__))



# Classify API
sonar = Sonar()
stemmer = PorterStemmer()
def classify ():
    try:
        hateSentence = request.json['sentence']
        # print (hateSentence)
        if (hateSentence == ''):
            return '0'
    except:
        return '0'

    try:
        result = sonar.ping(hateSentence)
        if result['top_class']=="neither":
            stemmed_sent = " ".join(list(map(stemmer.stem,hateSentence.split())))
            result = sonar.ping(stemmed_sent)
            # print('stem ', result, stemmed_sent)

        rc = result['classes']
        max_hate = 0
        total_hate = 0
        # print (rc)
        for c in rc:
            if (c['class_name'] == 'hate_speech'):
                max_hate = max(max_hate, c['confidence'])
                total_hate += c['confidence']
            elif (c['class_name'] == 'offensive_language'):
                max_hate = max(max_hate, c['confidence'])
                total_hate += c['confidence']

        # print (max_hate, total_hate)
        return str((1.0*max_hate + 1.0*total_hate) / 2.0)
    except:
        print ("Some error occured in classify")
        return '0'


# Hate to No-Hate API
def convert ():
    try:
        hateSentence = request.json['sentence']
        mode = request.json['mode']

        # print (request.json)
        # print (hateSentence)
        # print (conv.convert(hateSentence, mode=mode))
        result = conv.convert(hateSentence, mode=mode)
        # print (result)

        return jsonify({
            'intermediate': result[0],
            'final': result[1]
        })

    except:
        print ("Some error occured in convert")
        return jsonify({
            'intermediate': 'I pledge to speak decently',
            'final': 'I pledge to speak decently'
        })

