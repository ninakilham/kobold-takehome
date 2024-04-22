import sys
import unittest
from unittest import TestCase
import numpy as np
import pandas as pd
from pandas import testing as tm

sys.path.append('/Users/ninakilham/Documents/GitHub/kobold-takehome/src')
import utils as kutils


class test_utils(unittest.TestCase):

    def test_function(self):
        """Test quick function"""
        dfin = pd.DataFrame(data=[0.5, 0.5, 0.45, 0.6, 0.65, 0.7], columns=["var"])
        dfout = kutils.check_if_empty(dfin, var="var")

        tm.assert_frame_equal(dfin, dfout)

if __name__ == "__main__":
    unittest.main()
