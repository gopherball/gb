import gb.protocol


class Document:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def __str__(self):
        chunks = []

        for entry in self.entries:
            chunks.append(
                gb.protocol.template.format(e=entry) + gb.protocol.crlf
            )

        return "".join(chunks)
