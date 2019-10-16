import default
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../note'))
from note import sort_notes, get_notes_from_tags, get_notes_tonalities_indices

def count_semitones(notes):
    """ Returns the number of semitones between two notes """
    root_note, high_note = sort_notes(notes)
    return high_note.keyboard_index() - root_note.keyboard_index()

def get_delta_tones(notes):
    """ Returns tone's difference between two notes """
    i_root_note, i_high_note = get_notes_tonalities_indices(sort_notes(notes))
    if i_root_note <= i_high_note:
        return i_high_note - i_root_note
    else:
        return 7 + i_high_note - i_root_note

def get_flattened_interval(interval):
    """ Returns interval's closest base interval; ie returns a fourth if interval is an eleventh """
    n_notes_in_scale = 12
    flattened_semitones = interval.count_semitones() % n_notes_in_scale
    return Interval(flattened_semitones, interval.delta_tones())

class Interval:
    """
    class Interval

    Instances of this class describe an musical interval.
    An interval is defined by a number of semitones (between notes).
    Attribute delta_tone was introduced as (for instance) minor third and
    augmented ninth intervals are not different with regard to n_semitones.
    """
    def __init__(self, interval_n_semitones = default.n_semitones, interval_delta_tones = default.delta_tones):
        self._n_semitones = interval_n_semitones
        self._delta_tones = interval_delta_tones

    def count_semitones(self):
        return self._n_semitones

    def delta_tones(self):
        return self._delta_tones

    def __eq__(self, other):
        return self.count_semitones() == other.count_semitones() and self.delta_tones() == other.delta_tones()

    def from_notes(self, notes):
        self._n_semitones, self._delta_tones = count_semitones(notes), get_delta_tones(notes)
        return self

    def from_tags(self, notes_tags):
        """ Returns intervals from a list containing two notes tags """
        notes = get_notes_from_tags(notes_tags)
        self.from_notes(notes)
        return self
