import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from interval import Interval, get_flattened_interval
import intervals_factory

def test_make_default():
    tested_interval = Interval()
    return tested_interval == intervals_factory.make_major_third()

def test_make_custom():
    tested_interval = Interval().from_tags(['C4', 'F#4'])
    return tested_interval == intervals_factory.make_augmented_fourth()

def test_flattened_c4_to_f5():
    tested_interval = Interval().from_tags(['C4', 'F5'])
    return get_flattened_interval(tested_interval) == intervals_factory.make_fourth()

def test_flattened_c4_to_a5():
    tested_interval = Interval().from_tags(['C4', 'A5'])
    return get_flattened_interval(tested_interval) == intervals_factory.make_sixth()
