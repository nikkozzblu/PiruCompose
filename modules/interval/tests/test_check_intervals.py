import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from interval import Interval
import check_intervals

def test_check_major_third():
    return check_intervals.is_major_third(Interval().from_tags(['G4', 'B7']))
