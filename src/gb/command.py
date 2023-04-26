import sys
import ipaddress
import logging

import click
import tornado.iostream

import gb.server


log = logging.getLogger(__name__)

modes = {
    "implicit": gb.server.ImplicitGopherServer,
}


def bail(message: str) -> None:
    """Write a message to stderr and exit unsuccesfully."""
    print(message, file=sys.stderr)
    raise SystemExit(1)


@click.command()
@click.option(
    "--mode",
    "-m",
    required=True,
    type=click.Choice([str(mode) for mode in modes.keys()]),
    help="Mode to run as.",
)
@click.option(
    "--host",
    "-h",
    default="127.0.0.1",
    show_default=True,
    help="IP address to listen on.",
)
@click.option(
    "--port", "-p", default=7070, show_default=True, help="Port to listen on."
)
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Verbosity, passing more heightens the verbosity.",
)
@click.option(
    "--magic",
    default=False,
    help="Enable magic mode to try and guess filetypes by extension and content.",
    show_default=True,
    is_flag=True,
)
@click.option(
    "--utf8",
    "-u",
    default=False,
    help="Use UTF-8 as the default encoding instead of the standard ISO-8859-1",
    is_flag=True,
)
@click.argument(
    "path", required=True, type=click.Path(exists=True), envvar="GB_PATH"
)
def main(
    mode: str,
    host: str,
    port: int,
    path: click.Path,
    verbose: int,
    magic: bool,
    utf8: bool,
) -> int:
    """`gb` or gopherball is a modern server for the Gopher protocol."""

    if port < 0 or port > 65535:
        bail("Invalid port supplied.")

    try:
        host = str(ipaddress.ip_address(host))
    except ValueError:
        bail("Unparseable IP supplied.")

    if mode not in modes:
        bail("Invalid mode supplied.")

    if utf8:
        encoding = "utf8"
    else:
        encoding = "iso-8859-1"

    logging.basicConfig(level=logging.INFO)

    server = modes[mode](str(path), "localhost", 7070, magic, encoding)
    server.listen(port)
    server.start(0)

    tornado.ioloop.IOLoop.current().start()

    return 0


if __name__ == "__main__":
    raise SystemExit(main(auto_envvar_prefix="GB"))
