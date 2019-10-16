import tuning
import note

def make(tuning = tuning.regular_guitar):
    return Strings_instrument().set_tuning(tuning)

def make_regular_guitar():
    return make(tuning = tuning.regular_guitar)

class Strings_instrument:
    """
    class String_instrument describes an instrument with strings and frets
    """
    def __init__(self):
        self._tuning = note.get_keyboard_indices(tuning.regular_guitar)
        self.init_frets()

    def count_strings(self):
        return len(self._tuning)

    def init_frets(self):
        self._frets = [None] * self.count_strings()
        return self

    def set_tuning(self, tuning):
        self._tuning = note.get_keyboard_indices(tuning)
        self.init_frets()
        return self

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
