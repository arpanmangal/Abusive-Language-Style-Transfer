# Imports the Google Cloud client library
from google.cloud import translate
import re
from tqdm import tqdm

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



if __name__ == '__main__':
	# Testing static code
	ffile = open('test.fr', 'w')
	for line in tqdm(open('test.en', 'r')):
		text = line
		target = 'hi'

		# Translates some text into Russian
		translation = translate_client.translate(
			text,
			target_language=target)

		result = re.sub("&#39;", "'", translation['translatedText'])
		ffile.write(u'{}'.format(result))
		ffile.write(u'\n')
		# print(u'Text: {}'.format(text))
		# print(u'Translation: {}'.format(result))
		# print (result)
	ffile.close()

	enfile = open('out.en', 'w')
	for line in tqdm(open('test.fr', 'r')):
		text = line
		target = 'en'

		# Translates some text into Russian
		translation = translate_client.translate(
			text,
			target_language=target)

		result = re.sub("&#39;", "'", translation['translatedText'])
		enfile.write(u'{}'.format(result))
		enfile.write(u'\n')
	enfile.close()
