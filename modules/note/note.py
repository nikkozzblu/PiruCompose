import tonality
import alteration
import octave
from utils import get_tonality, get_alteration, get_octave
import keyboard
from tone import Tone

def get_notes_from_tags(notes_tags):
    """ Builds Note() instances from a list of tag """
    return [Note().from_tag(tag) for tag in notes_tags]

def get_notes_keyboard_indices_from_tags(tags):
    """ Returns keyboard's keys indices refering to a list of note's tags """
    return [keyboard.notes[tag] for tag in tags]

def get_notes_keyboard_indices(notes):
    """ Returns keyboard's keys indices refering to a list of notes """
    return [note.keyboard_index() for note in notes]

def sort_notes(notes):
    """ Returns a copy of notes sorted by increasing height """
    return sorted(notes, key = lambda note: note.keyboard_index())

def get_notes_tonalities(notes):
    """ Returns tonalities of a list of notes """
    return [note.tonality() for note in notes]

def get_notes_tonalities_indices(notes):
    """ Returns tonalities indices refering to a list of notes """
    return [tonality.valid_values.index(current_tonality) for current_tonality in get_notes_tonalities(notes)]

class Note:
    """
    class Note

    Instances of these class can be used to manipulatemusic notes.
    The difference with an instance of Tone() is the notion of 'octave' (ear height).
    """
    def __init__(self, note_tonality = tonality.default_value, note_alteration = alteration.default_value, note_octave = octave.default_value):
        self._tone   = Tone(note_tonality, note_alteration)
        self._octave = note_octave

    def tonality(self):
        return self._tone.tonality()

    def tag(self):
        return self._tone.tag() + self._octave

    def keyboard_index(self):
        return keyboard.notes[self.tag()]

    def from_tag(self, tag):
        note_tonality, note_alteration, note_octave = get_tonality(tag), get_alteration(tag), get_octave(tag)
        self._tone, self._octave = Tone(note_tonality, note_alteration), note_octave
        return self
