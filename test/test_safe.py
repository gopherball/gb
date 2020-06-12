import pytest

import gb.safe


def test_relativize():
    with pytest.raises(Exception):
        gb.safe.relativize("/tmp", "../../../")
