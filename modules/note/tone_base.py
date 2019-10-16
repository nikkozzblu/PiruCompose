from utils import get_tonality, get_alteration
import tonality
import alteration

class Tone_base:
    """
    class Tone :
    
    Properties class for tone's decription.
    A tonality and an alteration describes a tone.
    """
    def __init__(self, custom_tonality = tonality.default_value, custom_alteration = alteration.default_value):
        self._tonality   = custom_tonality
        self._alteration = custom_alteration

    def tonality(self):
        return self._tonality

    def alteration(self):
        return self._alteration

    def from_tag(self, tag):
        self._tonality, self._alteration = get_tonality(tag), get_alteration(tag)
        return self

