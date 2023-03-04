import locale
import logging

from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    language, _ = locale.getdefaultlocale()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Initializing for language %s...', language)
    client = CloudSpeechClient()
    with Board() as board:
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
                pass

if __name__ == '__main__':
    main()