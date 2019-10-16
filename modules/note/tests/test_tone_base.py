import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tonality
import alteration
from tone_base import Tone_base


def test_make_valid():
    tested_tone_base = Tone_base('G', 'b')
    return tested_tone_base.tonality() == 'G' and tested_tone_base.alteration() == 'b'

def test_make_invalid():
    tested_tone_base = Tone_base('H', 'j')
    return tested_tone_base.tonality() == tonality.default_value and tested_tone_base.alteration() == alteration.default_value

