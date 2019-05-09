# Imports the Google Cloud client library
from google.cloud import translate
import re

# Instantiates a client
translate_client = translate.Client()

def translate (sentence, target='fr'):
	if (target != 'fr' and target != 'ru' and  target != 'hi'):
		target = 'fr'

	text = u'{}'.format(sentence)
	translation = translate_client.translate(
		text,
		target_language=target)

	translated = u'{}'.format(re.sub("&#39;", "'", translation['translatedText']))

	backtranslation = translate_client.translate(
		translated,
		target_language='en')

	backtranslated = u'{}'.format(re.sub("&#39;", "'", backtranslation['translatedText']))
	return translated, backtranslated
