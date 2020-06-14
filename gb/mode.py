import os

import gb.protocol
import gb.document
import gb.entry
import gb.safe
import gb.magic


class Mode:
    def __init__(self, base_path: str, magic: bool) -> None:
        self.base_path = os.path.abspath(base_path)
        self.magic = magic

    def lookup(self, path: str) -> str:
        raise NotImplementedError()


class ImplicitMode(Mode):
    """ImplicitMode looks up files recursively within a given path auto-
       generating any required indexes."""

    def lookup(self, path: str) -> str:
        """Look up a path within our base path and return the contents in
           pre-rendered Gopher format!"""

        path = gb.safe.relativize(self.base_path, path)

        if os.path.islink(path):
            raise ValueError()

        if os.path.isdir(path):
            return self._directory(path)
        elif os.path.isfile(path):
            return self._file(path)
        else:
            raise ValueError()

    def _directory(self, path: str) -> str:
        """Render the files in a directory as gopher data."""

        response = gb.document.Document()

        for entry in os.listdir(path):
            entry = os.path.join(path, entry)

            if os.path.isdir(entry):
                item = gb.entry.Directory
            elif os.path.isfile(entry):
                if self.magic:
                    item = gb.magic.guess_type(entry)  # type: ignore
                else:
                    item = gb.entry.Binary  # type: ignore

            response.add_entry(
                item(os.path.basename(entry), entry[len(self.base_path) :])
            )

        return str(response)

    def _file(self, path: str) -> str:
        # XXX this fails when in utf8 (or in general), read bytes and then
        # XXX either use surrogateescape (or just return bytes) or only do
        # XXX so for non-readable files
        with open(path) as f:
            return f.read()
