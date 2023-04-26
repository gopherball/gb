import os


def relativize(base: str, path: str) -> str:
    """Join base and path making sure that the resulting path lies
    within the base. We do this by making path relative if it's an
    absolute path then verifying if it's still within the base after
    joining.

    We fail hard if the calculated path is not within base."""

    base = os.path.abspath(base)

    # The nif the path starts with a separator we remove that
    if path.startswith(os.path.sep):
        path = path[len(os.path.sep) :]

    dest = os.path.join(base, path)
    dest = os.path.abspath(dest)

    if os.path.commonprefix([base, dest]) != base:
        # TODO we want a better way to communicate this to our server
        # TODO so it can cleanly close the connection
        raise Exception("welp")

    return dest
