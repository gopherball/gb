import unittest

import gb.protocol


class TestProtocolCleanSelector(unittest.TestCase):
    def test_empty_selector(self,):
        assert "/" == gb.protocol.clean_selector("\r\n")
        assert "/" == gb.protocol.clean_selector("\n")

    def test_word_selector(self,):
        assert "foo" == gb.protocol.clean_selector("foo\r\n")
        assert "foo" == gb.protocol.clean_selector("foo\n")
