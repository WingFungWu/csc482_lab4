import locale, logging, re, command

from aiy.cloudspeech import CloudSpeechClient
from aiy.voice.tts import say
from aiy.board import Board, Led

def main():
    language, _ = locale.getdefaultlocale()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Initializing for language %s...', language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            board.button.wait_for_press()
            logging.info('Say something after you press the button.')
            board.led.state = Led.ON
            q = client.recognize(language_code=language)
            board.button.wait_for_release()
            board.led.state = Led.OFF
            
            if q is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % q)
            if re.search(r'goodbye|bye|exit|quit', q):
                break
            else:
                a = command.run_command(q)
                logging.info('Response: "%s"' % a)
                say(a)

if __name__ == '__main__':
    main()