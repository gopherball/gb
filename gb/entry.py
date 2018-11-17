import gb.protocol


class Entry:
    host = "localhost"
    port = "7070"

    def __init__(self, text, selector):
        self.text = text
        self.selector = selector


class Text(Entry):
    code = 0


class Directory(Entry):
    code = 1

    def __init__(self, text, selector):
        self.text = text + "/"
        self.selector = selector


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
