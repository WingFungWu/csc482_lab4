import locale
import logging

from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.tts import say
from chatbot import chat

def main():
    language, _ = locale.getdefaultlocale()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Initializing for language %s...', language)
    client = CloudSpeechClient()
    while True:
        logging.info('Say something.')
        q = client.recognize(language_code=language)
        if q is None:
            logging.info('You said nothing.')
            continue

        logging.info('You said: "%s"' % q)
        q = q.lower()
        if 'goodbye' in q:
            break
        else:
            a = chat.respond(q)
            say(a)
            

if __name__ == '__main__':
    main()