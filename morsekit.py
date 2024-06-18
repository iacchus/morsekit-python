#!/usr/bin/env python

import subprocess

# https://en.wikipedia.org/wiki/Morse_code

DIT_DURATION = 0.1
DAH_DURATION = DIT_DURATION * 3
SIGNAL_SPACE_DURATION = DIT_DURATION  # space between signals of one letter
LETTER_SPACE_DURATION = DIT_DURATION * 3 # duration of space between letters
WORD_SPACE_DURATION = DIT_DURATION * 7

FREQUENCY_SOUND = 1760  # A6
FREQUENCY_PAUSE = 0  # silence
PLAY_COMMAND = "play -n synth {duration} sin {frequency}"

SIGNAL_TABLE = {
        '.': 0,
        '-': 1,
        '#': 2,  # between signals (inside letter, ie., same letter)
        '=': 3,  # between letters (ie., same word)
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

    0: short
    1: long
    2: signal pause
    3: letter pause
    4: word pause
    """

    command = PLAY_COMMAND.format(**SIGNAL_ARGS[signal]).split(' ')

    #  print(' '.join(command))

    # https://docs.python.org/3/library/subprocess.html#subprocess.run
    subprocess.run(command, capture_output=True)

def encode_word(word: str):
    #  encoded_word = '#'.join([MORSE_TABLE[letter.lower()] for letter in word])
    morse_word = ''.join([MORSE_TABLE[letter.lower()] for letter in word])
    encoded_word = '#'.join(morse_word)
    #  print(encoded_word)

    return encoded_word

w = 'abba baba'

list_of_words = w.split(' ')

#  encoded_words = '='.join([encode_word(word) for word in list_of_words])
#  encoded_words = '='.join([encode_word(word) for word in list_of_words])
encoded_words = [encode_word(word) for word in list_of_words]

encoded = ' '.join(encoded_words)

#  print(encoded_words)
#  print(w, list_of_words, encoded_words, encoded, sep='\n')
#  code = ''.join([MORSE_TABLE[letter] for letter in w])

#  print(code)
print(encoded)

for signal in encoded:
    print(signal)
    play_signal(signal=SIGNAL_TABLE[signal])

