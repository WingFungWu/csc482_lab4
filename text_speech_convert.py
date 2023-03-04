import locale
import logging

from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.tts import say

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    language, _ = locale.getdefaultlocale()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Initializing for language %s...', language)
    client = CloudSpeechClient()
    while True:
        logging.info('Say something.')
        text = client.recognize(language_code=language)
        if text is None:
            logging.info('You said nothing.')
            continue

        logging.info('You said: "%s"' % text)
        text = text.lower()
        if 'goodbye' in text:
            break
        else:
            say(text)

if __name__ == '__main__':
    main()