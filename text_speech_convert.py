import locale
import logging

from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.tts import say
import sys
sys.path.insert(1, '/home/pi/csc482_lab4/CSChatBot-main')
import chatbot, sql_queries

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
            bot = chatbot.ChatBot()
            print("Hello I am EKK, your Cal Poly Virtual Assistant. How can I help you today?")
            q = text
            entities, answer = bot.get_sample_answers(q)
            if answer != -1:
                query = sql_queries.Query(q, entities, answer)
                query.queryDB()
            

if __name__ == '__main__':
    main()