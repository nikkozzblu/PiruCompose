import default
import utils
import tone
import keyboard

def make(
tonality   = default.tonality  ,
alteration = default.alteration,
octave     = default.octave
):
    """ Custom static constructor of Note() instances """
    return Note().set_tone(tone.make(tonality, alteration)).set_octave(octave)

def from_tag(tag):
    """ Builds Note() instance from tag """
    tonality, alteration, octave = utils.get_tonality(tag), utils.get_alteration(tag), utils.get_octave(tag)
    return Note().set_tone(tone.make(tonality, alteration)).set_octave(octave)

class Note:
    """
    class Note

    Instances of these class can be used to manipulatemusic notes.
    The difference with an instance of Tone() is the notion of 'octave' (ear height).
    """
    def __init__(self):
        self._tone   = tone.make()
        self._octave = default.octave

    def set_tone(self, tone):
        self._tone = tone
        return self

    def set_octave(self, octave):
        if octave in default.valid_octaves:
            self._octave = octave
        return self

    def tag(self):
        return self._tone.tag() + self._octave

    def keyboard_index(self):
        return keyboard.notes[self.tag()]

