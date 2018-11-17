import logging

log = logging.getLogger(__name__)

crlf = "\r\n"
eof = "."

template = "{e.code}{e.text}\t{e.selector}\t{e.host}\t{e.port}"


def clean_selector(selector):
    """Strip the end off of a selector and normalize an empty one."""
    selector = selector.rstrip(crlf)

    if selector == "":
        selector = "/"

    return selector


def is_valid_selector(selector):
    """Validate the selector according to gopher rules."""

    # TODO implement <TAB> denoted search

    # These characters are forbidden in gopher selectors and should immediately
    # terminate the connection
    return not any(forbidden in selector for forbidden in "\t\r\n")
