from typing import List

import gb.protocol
import gb.entry


class Document:
    """A document is an index of entries for a certain directory. It dictates
    how those entries are joined together and if any extra information is
    added."""

    entries: List[gb.entry.Entry]

    def __init__(self) -> None:
        self.entries = []

    def add_entry(self, entry: gb.entry.Entry) -> None:
        self.entries.append(entry)

    def __str__(self) -> str:
        return (
            gb.protocol.crlf.join(
                gb.protocol.template.format(e=e) for e in self.entries
            )
            + gb.protocol.crlf
        )
