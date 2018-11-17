import gb.protocol


class Document:
    """A document is and index of entries for a certain directory. It dictates
      how those entries are joined together and if any extra information is
      added."""

    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def __str__(self):
        return (
            gb.protocol.crlf.join(
                gb.protocol.template.format(e=e) for e in self.entries
            )
            + gb.protocol.crlf
        )
