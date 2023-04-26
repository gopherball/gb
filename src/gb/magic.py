from typing import Union, Type, Text

import magic

import gb.entry


mime_entry = {"text": gb.entry.Text}


def guess_type(path: str) -> Union[Type[Text], str, None]:
    """Guess the type of a path and return the corresponding Entry for that
    type with its data loaded."""

    guess = magic.Magic(mime=True).from_file(path).split("/")[0]
    return mime_entry.get(guess, gb.entry.Binary)  # type: ignore
