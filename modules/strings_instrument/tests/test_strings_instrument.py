import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import strings_instrument


def test_play_single_note_natural_c():
    tested_instrument = strings_instrument.make_regular_guitar()
    i_natural_c = 39
    a_string, c_fret = 1, 3
    return tested_instrument.play_single_note(a_string, c_fret) == i_natural_c
