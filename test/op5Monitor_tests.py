import sys
import os
sys.path.append(os.path.abspath('../Nagstamon/Nagstamon'))
from Nagstamon.Server import op5Monitor

def test_human_duration_3days_difference():
    assert (op5Monitor.human_duration(1397600000, 1397859200) == "kalle")
