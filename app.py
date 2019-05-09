#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# Additional Imports
#----------------------------------------------------------------------------#
PATH = os.path.dirname(os.path.abspath(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(PATH, "model/service.json")
print (PATH)
from flask import jsonify
from flask import send_from_directory, current_app as app
import json
import model.convert as conv
from hatesonar import Sonar
from nltk.stem import PorterStemmer


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
# app.config.from_object('config')

### Load your model over here ###
model = lambda x: x

def predict(input):
    return "I don't use it!"

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
@app.route('/', methods=['GET'])
def home():
    return send_from_directory ('templates/', 'index.html')
    # if request.method == 'POST':
    #     ## Called after submit button is clicked
    #     output = predict(request.form['input_text'])
    #     template = render_template('project.html', result=output)
    #     return template

    # if request.method == 'GET':
    #     return render_template('project.html')


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


#----------------------------------------------------------------------------#
# My Controllers.
# Functions imported from models/convert.py
#----------------------------------------------------------------------------#
sonar = Sonar()
stemmer = PorterStemmer()

@app.route('/classify', methods=['POST'])
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


@app.route('/convert', methods=['POST'])
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


@app.route('/report.pdf')
def show_report_pdf():
    return send_from_directory('model', 'report.pdf')


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

