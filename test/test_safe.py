import unittest

import gb.safe


class TestSafeRelativize(unittest.TestCase):
    def test_relative_path(self):
        with self.assertRaises(Exception):
            gb.safe.relativize("/tmp", "../../../")
