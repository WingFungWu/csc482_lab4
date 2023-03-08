import locale, logging, re, numeric

from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.tts import say

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
        if re.search(r'goodbye|bye|exit|quit', q):
            break
        else:
            a = numeric.main(q)
            logging.info('Response: "%s"' % a)
            say(a)

if __name__ == '__main__':
    main()