class Entry:
    """Gopher indexes contain entries of various types. This list is both
       sourced from RFC 1436:

       https://tools.ietf.org/html/rfc1436

       and the Wikipedia page for non-standard types:

       https://en.wikipedia.org/wiki/Gopher_(protocol)#Item_types"""

    host: str
    port: int

    def __init__(self, host: str, port: int, text: str, selector: str) -> None:
        self.host = host
        self.port = port

        self.text = text
        self.selector = selector


class Text(Entry):
    code = 0


class Directory(Entry):
    code = 1

    def __init__(self, host: str, port: int, text: str, selector: str) -> None:
        super().__init__(host, port, text, selector)

        self.text = text + "/"


class CCSO(Entry):
    code = 2


class Error(Entry):
    code = 3


class BinHex(Entry):
    code = 4


class DOS(Entry):
    code = 5


class UU(Entry):
    code = 6


class Search(Entry):
    code = 7


class Telnet(Entry):
    code = 8


class Binary(Entry):
    code = 9


class Mirror(Entry):
    code = "+"


class GIF(Entry):
    code = "g"


class Image(Entry):
    code = "I"


class Telnet3270(Entry):
    code = "T"


class HTML(Entry):
    code = "h"


class Information(Entry):
    code = "i"


class Sound(Entry):
    code = "s"
