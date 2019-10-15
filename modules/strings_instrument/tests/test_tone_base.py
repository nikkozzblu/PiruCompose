import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import default
import tone_base


def test_make_valid():
    tonality, alteration = 'G', 'b'
    tested_tone_base = tone_base.make(tonality, alteration)
    return tested_tone_base.tonality() == tonality and tested_tone_base.alteration() == alteration

def test_make_invalid():
    tonality, alteration = 'H', 'j'
    tested_tone_base = tone_base.make(tonality, alteration)
    return tested_tone_base.tonality() == default.tonality and tested_tone_base.alteration() == default.alteration

