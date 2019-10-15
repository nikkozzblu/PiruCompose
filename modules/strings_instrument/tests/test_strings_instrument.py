import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import strings_instrument

def test_play_full_palm_mute_guitar():
    tested_instrument = strings_instrument.make_regular_guitar()
    return tested_instrument.play_strings() == [None] * 6

def test_play_natural_c_guitar():
    tested_instrument = strings_instrument.make_regular_guitar()
    tested_instrument.press_strings([None, 3, None, None, None, None])
    return tested_instrument.play_strings() == [None, 39, None, None, None, None]

def test_play_regular_c_chord_guitar():
    tested_instrument = strings_instrument.make_regular_guitar()
    tested_instrument.press_strings([None, 3, 2, 0, 1, None])
    return tested_instrument.play_strings() == [None, 39, 43, 46, 51, None]
