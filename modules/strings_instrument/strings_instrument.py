import tuning
import keyboard


def make(tuning = tuning.regular_guitar):
    return String_instrument().set_tuning(tuning)

def make_regular_guitar():
    return make(tuning = tuning.regular_guitar)


class String_instrument:
    """
    class String_instrument describes an instrument with strings and frets
    """
    def __init__(self):
        self._tuning = tuning.regular_guitar

    def set_tuning(self, tuning):
        self._tuning = tuning
        return self

    def play_single_note(self, i_string, i_fret) :
        open_string_tag = self._tuning[i_string]
        return keyboard.notes[open_string_tag] + i_fret if i_fret != None else None

