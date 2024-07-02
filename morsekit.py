#!/usr/bin/env python

import subprocess

# https://en.wikipedia.org/wiki/Morse_code

DIT_DURATION = 0.1
DAH_DURATION = round(DIT_DURATION * 3, 3)
SIGNAL_SPACE_DURATION = DIT_DURATION  # space between signals of one letter
LETTER_SPACE_DURATION = round(DIT_DURATION * 3, 3) # duration of space between letters
WORD_SPACE_DURATION = round(DIT_DURATION * 7, 3)  # space between words

FREQUENCY_SOUND = 1760  # A6
FREQUENCY_PAUSE = 0  # silence
PLAY_COMMAND = "play -n"
SIGNAL_ARGS_STR = "synth {duration} sin {frequency}"

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
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '.-',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': ' ',
        }

MORSE_REVERSE_TABLE = {code: letter for letter, code in MORSE_TABLE.items()}


def play(text: str):

    encoded_text = '='.join(['#'.join(MORSE_TABLE[character.lower()]) for character in text])

    print("encoded text is:", encoded_text)

    signal_args_list = list()
    for signal in encoded_text:
        signal_index = SIGNAL_TABLE[signal]
        signal_args_list.append(SIGNAL_ARGS_STR.format(**SIGNAL_ARGS[signal_index]))

    # https://stackoverflow.com/questions/46057100/how-to-sox-sequence-of-synth-commands
    signal_args = " : ".join(signal_args_list)
    command = f"{PLAY_COMMAND} {signal_args}".split(' ')

    print("command is:", ' '.join(command))

    # https://docs.python.org/3/library/subprocess.html#subprocess.run
    subprocess.run(command, capture_output=True)


if __name__ == "__main__":
    text = 'abba baba'

    play(text)
