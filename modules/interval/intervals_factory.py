from interval import Interval

def make_diminished_ninth():
    """ Returns diminished ninth interval (ie C to Db) """
    return Interval(interval_n_semitones = 1, interval_delta_tones = 1)

def make_ninth():
    """ Returns ninth interval (ie C to D) """
    return Interval(interval_n_semitones = 2, interval_delta_tones = 1)

def make_augmented_ninth():
    """ Returns augmented ninth interval (ie Bb to C#) """
    return Interval(interval_n_semitones = 3, interval_delta_tones = 1)

def make_minor_third():
    """ Returns minor third interval (ie C to Eb) """
    return Interval(interval_n_semitones = 3, interval_delta_tones = 2)

def make_major_third():
    """ Returns major third interval (ie C to E) """
    return Interval(interval_n_semitones = 4, interval_delta_tones = 2)

def make_augmented_third():
    """ Returns augmented third interval (ie Cb to E) """
    return Interval(interval_n_semitones = 5, interval_delta_tones = 2)

def make_diminished_fourth():
    """ Returns diminished fourth interval (ie B to Eb) """
    return Interval(interval_n_semitones = 4, interval_delta_tones = 3)

def make_fourth():
    """ Returns fourth interval (ie C to F) """
    return Interval(interval_n_semitones = 5, interval_delta_tones = 3)

def make_augmented_fourth():
    """ Returns augmented fourth interval (ie C to F#) """
    return Interval(interval_n_semitones = 6, interval_delta_tones = 3)

def make_diminished_fifth():
    """ Returns diminished fifth interval (ie C to Gb) """
    return Interval(interval_n_semitones = 6, interval_delta_tones = 4)

def make_fifth():
    """ Returns fifth interval (ie C to G) """
    return Interval(interval_n_semitones = 7, interval_delta_tones = 4)

def make_augmented_fifth():
    """ Returns augmented fifth interval (ie C to G#) """
    return Interval(interval_n_semitones = 8, interval_delta_tones = 4)

def make_diminished_sixth():
    """ Returns diminished sixth interval (ie C to Ab) """
    return Interval(interval_n_semitones = 8, interval_delta_tones = 5)

def make_sixth():
    """ Returns sixth interval (ie C to A) """
    return Interval(interval_n_semitones = 9, interval_delta_tones = 5)

def make_augmented_sixth():
    """ Returns augmented sixth interval (ie C to A#) """
    return Interval(interval_n_semitones = 10, interval_delta_tones = 5)

def make_minor_seventh():
    """ Returns minor seventh interval (ie C to Bb) """
    return Interval(interval_n_semitones = 10, interval_delta_tones = 6)

def make_major_seventh():
    """ Returns major seventh interval (ie C to B) """
    return Interval(interval_n_semitones = 11, interval_delta_tones = 6)

def make_augmented_seventh():
    """ Returns augmented seventh interval (ie Cb to B) """
    return Interval(interval_n_semitones = 12, interval_delta_tones = 6)

