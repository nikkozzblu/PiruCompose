import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tonality
import alteration
from tone import Tone

def test_make_valid():
    tested_tone = Tone().from_tag('Gb')
    return tested_tone.tag() == 'Gb'

def test_make_invalid():
    tested_tone = Tone().from_tag('Hj')
    return tested_tone.tag() == tonality.default_value + alteration.default_value

def test_from_valid_tag_Asharp():
    tag = 'A#'
    tested_tone = Tone().from_tag(tag)
    return tested_tone.tag() == tag

def test_from_valid_tag_F():
    tag = 'F'
    tested_tone = Tone().from_tag(tag)
    return tested_tone.tag() == tag

def test_from_valid_tag_Eb():
    tag = 'Eb'
    tested_tone = Tone().from_tag(tag)
    return tested_tone.tag() == tag

def test_from_invalid_tag():
    tag = 'Hj'
    tested_tone = Tone().from_tag(tag)
    return tested_tone.tag() == tonality.default_value + alteration.default_value

