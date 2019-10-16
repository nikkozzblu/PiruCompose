import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import default
import note

def test_default_tag():
    tested_note = note.make()
    return tested_note.tag() == default.tonality + default.alteration + default.octave

def test_default_index():
    tested_note = note.make()
    return tested_note.keyboard_index() == 48

def test_custom_tag():
    tonality, alteration, octave = 'F', '#', '5'
    tested_note = note.make(tonality = tonality, alteration = alteration, octave = octave)
    return tested_note.tag() == tonality + alteration + octave

def test_custom_index():
    tonality, alteration, octave = 'F', '#', '5'
    tested_note = note.make(tonality = tonality, alteration = alteration, octave = octave)
    return tested_note.keyboard_index() == 57

def test_tag_from_valid_tag_Asharp3():
    tag = 'A#3'
    tested_note = note.from_tag(tag)
    return tested_note.tag() == tag

def test_keyboard_index_from_valid_tag_Asharp3():
    tag = 'A#3'
    tested_note = note.from_tag(tag)
    return tested_note.keyboard_index() == 37
