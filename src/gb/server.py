import logging

from typing import Tuple, Any

import tornado.tcpserver
import tornado.iostream

import gb.protocol
import gb.mode


log = logging.getLogger(__name__)


class GopherServer(tornado.tcpserver.TCPServer):
    """Generic tornado TCPServer which speaks the Gopher protocol. The Gopher
    protocol is defined in RFC 1436:

    https://tools.ietf.org/html/rfc1436."""

    # XXX TODO has to come from somewhere!
    encoding: str
    mode: gb.mode.Mode

    async def handle_stream(
        self, stream: tornado.iostream.IOStream, address: Tuple[Any, ...]
    ) -> None:
        """A new incoming connection. We wait silently until the client sends
        a selector through after which we clean and parse that selector."""

        log.debug("Accepted connection from %s", address)

        while True:
            try:
                # clean this up, split on \n but clean both
                selector_raw = await stream.read_until(
                    gb.protocol.crlf.encode(self.encoding),
                )
                selector_dec = selector_raw.decode(self.encoding)

                # clean this up, split on \n but clean both with \r
                selector_dec = gb.protocol.clean_selector(selector_dec)

                # If this is not a valid selector we immediately terminate
                # the connection
                if not gb.protocol.is_valid_selector(selector_dec):
                    log.warn(
                        "%s requested invalid selector %r, terminating.",
                        address,
                        selector_dec,
                    )
                    await self.close_stream(stream)
                    break

                log.info("%s requested %r", address, selector_dec)

                # Use our mode specific lookup to get our response
                resp_raw = await self.lookup(stream, selector_dec)
                resp_enc = resp_raw.encode(self.encoding)

                # Write and exit the connection
                await stream.write(resp_enc)
                await self.close_stream(stream)
            except ValueError:
                log.warning("Looking up selector %r failed", selector_dec)
                await self.close_stream(stream)
                break
            except tornado.iostream.StreamClosedError:
                log.debug("Lost connection from %s", address)
                break

    async def close_stream(self, stream: tornado.iostream.IOStream) -> None:
        """Gopher connections are closed by writing a . on a single line then
        closing the underlying transport."""
        await stream.write(gb.protocol.eof.encode(self.encoding))
        await stream.write(gb.protocol.crlf.encode(self.encoding))
        stream.close()

    async def lookup(self, stream: tornado.iostream.IOStream, data: str) -> str:
        """Lookup a selector on our mode."""
        return self.mode.lookup(data)


class ImplicitGopherServer(GopherServer):
    """The implicit gopher server serves files from a given path recursively
    while auto generating indexes for directories. If magic is enabled then
    the mode will auto-guess filetypes."""

    def __init__(
        self, path: str, host: str, port: int, magic: bool, encoding: str
    ) -> None:
        super().__init__()

        log.info("Starting ImplicitGopherServer with path %s", path)

        self.encoding = encoding
        self.mode = gb.mode.ImplicitMode(path, host, port, magic)
