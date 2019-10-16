import tonality
import alteration
import octave
"""
This file gathers simple functions that are used by several classes or modules
"""

def get_tonality(tag):
    """ Returns tonality from chars list tag (returns empty list if invalid) """
    i_tonality = 0
    return tag[i_tonality] if(len(tag) > 0 and tag[i_tonality] in tonality.valid_values) else ''

def get_alteration(tag):
    """ Returns alteration from chars list tag (returns empty list if invalid) """
    i_alteration = 1
    return tag[i_alteration] if(len(tag) > 1 and tag[i_alteration] in alteration.valid_values) else ''

def get_octave(tag):
    """ Returns octave from chars list tag (returns empty list if invalid) """
    i_alteration = -1
    return tag[i_alteration] if(len(tag) > 1 and tag[i_alteration] in octave.valid_values) else ''

