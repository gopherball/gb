import pytest

import gb.protocol


@pytest.mark.parametrize("selector,result", [("\r\n", "/"), ("\n", "/")])
def test_empty_selector(selector: str, result: str) -> None:
    assert gb.protocol.clean_selector(selector) == result


@pytest.mark.parametrize(
    "selector,result", [("foo\r\n", "foo"), ("foo\n", "foo")]
)
def test_word_selector(selector: str, result: str) -> None:
    assert gb.protocol.clean_selector(selector) == result
