import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import default
import tone

def test_make_valid():
    tonality, alteration = 'G', 'b'
    tested_tone = tone.make(tonality, alteration)
    return tested_tone.tag() == 'Gb'

def test_make_invalid():
    tonality, alteration = 'H', 'j'
    tested_tone = tone.make(tonality, alteration)
    return tested_tone.tag() == default.tonality + default.alteration

def test_from_valid_tag_Asharp():
    tag = 'A#'
    tested_tone = tone.from_tag(tag)
    return tested_tone.tag() == tag

def test_from_valid_tag_F():
    tag = 'F'
    tested_tone = tone.from_tag(tag)
    return tested_tone.tag() == tag

def test_from_valid_tag_Eb():
    tag = 'Eb'
    tested_tone = tone.from_tag(tag)
    return tested_tone.tag() == tag

def test_from_invalid_tag():
    tag = 'Hj'
    tested_tone = tone.from_tag(tag)
    return tested_tone.tag() == default.tonality + default.alteration

