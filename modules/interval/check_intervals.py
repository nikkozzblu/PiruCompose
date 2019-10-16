from interval import Interval, get_flattened_interval
import intervals_factory

def is_diminished_ninth(tested_interval):
    """ Returns True if tested_interval is a diminished ninth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_diminished_ninth()

def is_ninth(tested_interval):
    """ Returns True if tested_interval is a regular ninth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_ninth()

def is_augmented_ninth(tested_interval):
    """ Returns True if tested_interval is an augmented ninth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_ninth()

def is_minor_third(tested_interval):
    """ Returns True if tested_interval is a minor third """
    return get_flattened_interval(tested_interval) == intervals_factory.make_minor_third()

def is_major_third(tested_interval):
    """ Returns True if tested_interval is a major third """
    return get_flattened_interval(tested_interval) == intervals_factory.make_major_third()

def is_augmented_third(tested_interval):
    """ Returns True if tested_interval is an augmented third """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_third()

def is_diminished_fourth(tested_interval):
    """ Returns True if tested_interval is a diminished fourth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_diminished_fourth()

def is_fourth(tested_interval):
    """ Returns True if tested_interval is a fourth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_fourth()

def is_augmented_fourth(tested_interval):
    """ Returns True if tested_interval is an augmented fourth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_fourth()

def is_diminished_fifth(tested_interval):
    """ Returns True if tested_interval is a diminished fifth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_diminished_fifth()

def is_fifth(tested_interval):
    """ Returns True if tested_interval is a fifth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_fifth()

def is_augmented_fifth(tested_interval):
    """ Returns True if tested_interval is an augmented fifth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_fifth()

def is_diminished_sixth(tested_interval):
    """ Returns True if tested_interval is a diminished sixth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_diminished_sixth()

def is_sixth(tested_interval):
    """ Returns True if tested_interval is a sixth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_sixth()

def is_augmented_sixth(tested_interval):
    """ Returns True if tested_interval is an augmented sixth """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_sixth()

def is_minor_seventh(tested_interval):
    """ Returns True if tested_interval is a minor seventh """
    return get_flattened_interval(tested_interval) == intervals_factory.make_minor_seventh()

def is_major_seventh(tested_interval):
    """ Returns True if tested_interval is a major seventh """
    return get_flattened_interval(tested_interval) == intervals_factory.make_major_seventh()

def is_augmented_seventh(tested_interval):
    """ Returns True if tested_interval is an augmented seventh """
    return get_flattened_interval(tested_interval) == intervals_factory.make_augmented_seventh()

