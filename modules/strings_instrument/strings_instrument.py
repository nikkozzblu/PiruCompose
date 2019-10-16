import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../note'))

import tuning
from note import get_notes_keyboard_indices_from_tags

def make_guitar():
    """ Builds an instance of Strings_instrument with EADGBE tuning """
    return Strings_instrument(instrument_tuning = tuning.guitar)

def make_mandolin():
    """ Builds an instance of Strings_instrument with GDAE tuning """
    return Strings_instrument(intrument_tuning = tuning.mandolin)

class Strings_instrument:
    """
    class String_instrument describes an instrument with strings and frets
    """
    def __init__(self, instrument_tuning = tuning.guitar):
        self._tuning = get_notes_keyboard_indices_from_tags(instrument_tuning)
        self._frets = [None] * self.count_strings()

    def count_strings(self):
        return len(self._tuning)

    def press_strings(self, frets):
        if len(frets) == self.count_strings():
           self._frets = frets
        return self

    def play_string(self, i_string):
        i_fret = self._frets[i_string]
        return self._tuning[i_string] + i_fret if i_fret != None else None

    def play_strings(self):
        n_strings = self.count_strings()
        return [self.play_string(i_string) for i_string in range(n_strings)]
