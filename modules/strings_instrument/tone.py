import default
import utils
import tone_base

def make(tonality = default.tonality, alteration = default.alteration):
    """ Custom static constructor of Tone instances """
    return Tone().set_base(tone_base.make(tonality, alteration))

def from_tag(tag):
    """ Builds tone from a chars list """
    tonality, alteration = utils.get_tonality(tag), utils.get_alteration(tag)
    return Tone().set_base(tone_base.make(tonality, alteration))

class Tone:
    """
    Class Tone :

    Instances of this class permit the manipulation of tones.
    """
    def __init__(self):
        self._base = tone_base.make()

    def set_base(self, base):
        self._base = base
        return self

    def tag(self):
        return self._base.tonality() + self._base.alteration()

