"""Autograding script"""

import os
import homework.generate_data as gd


def test_01():
    """Test app"""

    gd.run(n_drivers=100, n_timesheet=1000)
    assert os.path.exists("files/drivers.csv")
    assert os.path.exists("files/timesheet.csv")
