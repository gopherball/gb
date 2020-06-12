import pytest

import gb.safe


@pytest.mark.parametrize(
    "path0,path1",
    [
        ("/tmp", "../../../",),
        ("/tmp", "../tmp/foo/bar/../../../../etc/passwd"),
        ("/tmp", "../foo"),
        ("/tmp/foo", "../tmp/foo/../bar"),
    ],
)
def test_relativize_error(path0: str, path1: str,) -> None:
    with pytest.raises(Exception):
        gb.safe.relativize(
            path0, path1,
        )
