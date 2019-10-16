from utils import get_tonality, get_alteration
from tone_base import Tone_base
import tonality
import alteration

class Tone:
    """
    Class Tone :

    Instances of this class permit the manipulation of tones.
    """
    def __init__(self, tone_tonality = tonality.default_value, tone_alteration = alteration.default_value):
        self._base = Tone_base(tone_tonality, tone_alteration)

    def tonality(self):
        return self._base.tonality()

    def tag(self):
        return self._base.tonality() + self._base.alteration()

    def from_tag(self, tag):
        self._base = Tone_base().from_tag(tag)
        return self

