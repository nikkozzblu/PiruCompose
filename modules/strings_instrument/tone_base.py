import default

def make(tonality = default.tonality, alteration = default.alteration):
    """ Custom static constructor of Tone_base instances """
    return Tone_base().set_tonality(tonality).set_alteration(alteration)

class Tone_base:
    """
    class Tone :
    
    Properties class for tone's decription.
    A tonality and an alteration describes a tone.
    """
    def __init__(self):
        self._tonality   = default.tonality
        self._alteration = default.alteration

    def set_tonality(self, tonality):
        if tonality in default.valid_tonalities:
            self._tonality = tonality
        return self

    def set_alteration(self, alteration):
        if alteration in default.valid_alterations:
            self._alteration = alteration
        return self

    def tonality(self):
        return self._tonality

    def alteration(self):
        return self._alteration    
