import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tonality
import alteration
import octave
from note import Note, sort_notes, get_notes_from_tags, get_notes_tonalities, get_notes_keyboard_indices_from_tags, get_notes_keyboard_indices, get_notes_tonalities_indices

def test_default_tag():
    tested_note = Note()
    return tested_note.tag() == tonality.default_value + alteration.default_value + octave.default_value

def test_default_index():
    tested_note = Note()
    return tested_note.keyboard_index() == 48

def test_custom_tag():
    tested_note = Note('F', '#', '5')
    return tested_note.tag() == 'F#5'

def test_custom_index():
    tested_note = Note('F', '#', '5')
    return tested_note.keyboard_index() == 57

def test_tag_from_valid_tag_Asharp3():
    tag = 'A#3'
    tested_note = Note().from_tag(tag)
    return tested_note.tag() == tag

def test_keyboard_index_from_valid_tag_Asharp3():
    tag = 'A#3'
    tested_note = Note().from_tag(tag)
    return tested_note.keyboard_index() == 37

def test_sort():
    tested_notes = get_notes_from_tags(['D4', 'E4', 'C4', 'F4'])
    tested_tags = [current_note.tag() for current_note in sort_notes(tested_notes)]
    return tested_tags == ['C4', 'D4', 'E4', 'F4']

def test_get_tonalities():
    tested_notes = get_notes_from_tags(['D4', 'E4', 'C4', 'F4'])
    return get_notes_tonalities(tested_notes) == ['D', 'E', 'C', 'F']

def test_get_keyboard_indices_from_tags():
    tested_tags = ['D4', 'E4', 'C5', 'F5']
    return get_notes_keyboard_indices_from_tags(tested_tags) == [41, 43, 51, 56]

def test_get_keyboard_indices():
    tested_notes = get_notes_from_tags(['D4', 'E4', 'C5', 'F5'])
    return get_notes_keyboard_indices(tested_notes) == [41, 43, 51, 56]

def test_get_tonalities_indices():
    tested_notes = get_notes_from_tags(['D4', 'E4', 'C5', 'F5'])
    return get_notes_tonalities_indices(tested_notes) == [3, 4, 2, 5]
