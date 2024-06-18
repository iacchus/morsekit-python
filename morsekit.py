#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Morse_code

DIT_DURATION = 0.1
DAH_DURATION = 0.3
SPACE_DURATION = 0.3
WORD_SPACE_DURATION = 0.7

FREQUENCY_SOUND = 1760
FREQUENCY_PAUSE = 0
PLAY_COMMAND = "play -n synth {duration} sin {frequency}"

SIGNAL_TABLE = {
        '': 0,
        '.': 1,
        '-': 2,
        ' ': 3,
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
    pass

w = 'abba'

code = " ".join([MORSE_TABLE[letter] for letter in w])

print(code)
