#!/usr/bin/env python

import subprocess

# https://en.wikipedia.org/wiki/Morse_code

DIT_DURATION = 0.1
DAH_DURATION = DIT_DURATION * 3
SIGNAL_SPACE_DURATION = DIT_DURATION  # space between signals of one letter
LETTER_SPACE_DURATION = DIT_DURATION * 3 # duration of space between letters
WORD_SPACE_DURATION = DIT_DURATION * 7

#  DAH_DURATION = 0.3
#  SPACE_DURATION = DIT_DURATION * 3
#  WORD_SPACE_DURATION = 0.7

FREQUENCY_SOUND = 1760
FREQUENCY_PAUSE = 0
PLAY_COMMAND = "play -n synth {duration} sin {frequency}"

SIGNAL_TABLE = {
        '.': 0,
        '-': 1,
        '#': 2,  # inside letter
        '=': 3,  # between letters
        ' ': 4,  # between words
        }

SIGNAL_ARGS = {
    0: {"duration": DIT_DURATION, "frequency": FREQUENCY_SOUND},
    1: {"duration": DAH_DURATION, "frequency": FREQUENCY_SOUND},
    2: {"duration": SIGNAL_SPACE_DURATION, "frequency": FREQUENCY_PAUSE},
    3: {"duration": LETTER_SPACE_DURATION, "frequency": FREQUENCY_PAUSE},
    4: {"duration": WORD_SPACE_DURATION, "frequency": FREQUENCY_PAUSE},
        }

MORSE_TABLE = {
        'a': '.-',
        'b': '.---',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': '',
        'h': '',
        'i': '',
        'j': '',
        'k': '',
        'l': '',
        'm': '',
        'n': '',
        'o': '',
        'p': '',
        'q': '',
        'r': '',
        's': '',
        't': '',
        'u': '',
        'v': '',
        'w': '',
        'x': '',
        'y': '',
        'z': '',
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',
        '0': '',
        }

def play_signal(signal: int):
    """plays the signal

    0: letter pause
    1: short
    2: long
    2: word pause
    """

    command = PLAY_COMMAND.format(**SIGNAL_ARGS[signal]).split(' ')

    print(' '.join(command))

    # https://docs.python.org/3/library/subprocess.html#subprocess.run
    subprocess.run(command, capture_output=True)

w = 'abba baba'

list_of_words = w.split(' ')

encoded_words = ['='.join(word) for word in list_of_words]

print(w, list_of_words, encoded_words)
code = ''.join([MORSE_TABLE[letter] for letter in w])

print(code)

#  for signal in code:
#      print(signal)
#      play_signal(signal=SIGNAL_TABLE[signal])

