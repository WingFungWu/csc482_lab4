
import argparse
import os
import subprocess
import tempfile

RUN_DIR = '/run/user/%d' % os.getuid()

def say(text, lang='en-US', volume=60, pitch=130, speed=100, device='default'):
    data = "<volume level='%d'><pitch level='%d'><speed level='%d'>%s</speed></pitch></volume>" % \
           (volume, pitch, speed, text)
    with tempfile.NamedTemporaryFile(suffix='.wav', dir=RUN_DIR) as f:
       cmd = 'pico2wave --wave %s --lang %s "%s" && aplay -q -D %s %s' % \
             (f.name, lang, data, device, f.name)
       subprocess.check_call(cmd, shell=True)


def _main():
    parser = argparse.ArgumentParser(description='Text To Speech (pico2wave)')
    parser.add_argument('--lang', default='en-US')
    parser.add_argument('--volume', type=int, default=60)
    parser.add_argument('--pitch', type=int, default=130)
    parser.add_argument('--speed', type=int, default=100)
    parser.add_argument('--device', default='default')
    parser.add_argument('text', help='path to disk image file ')
    args = parser.parse_args()
    # text = args.text
    text = "test"
    say(text, lang=args.lang, volume=args.volume, pitch=args.pitch, speed=args.speed,
        device=args.device)


if __name__ == '__main__':
    _main()
