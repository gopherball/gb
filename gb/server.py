import logging

import tornado.tcpserver
import tornado.iostream

import gb.protocol
import gb.mode


log = logging.getLogger(__name__)


class GopherServer(tornado.tcpserver.TCPServer):
    async def handle_stream(self, stream, address):
        log.debug("Accepted connection from %s", address)

        while True:
            try:
                # clean this up, split on \n but clean both
                selector = await stream.read_until(b"\n")  # gb.protocol.crlf)
                selector = selector.decode("ascii")

                # clean this up, split on \n but clean both with \r
                selector = gb.protocol.clean_selector(selector)

                # If this is not a valid selector we immediately terminate
                # the connection
                if not gb.protocol.is_valid_selector(selector):
                    log.warn("%s requested invalid selector %r, terminating.", address, selector)
                    await self.close_stream(stream)
                    continue

                if not selector:
                    selector = "/"

                log.info("%s requested %r", address, selector)

                # Use our mode specific lookup to get our response
                resp = await self.lookup(stream, selector)
                resp = resp.encode("ascii")

                # Write and exit the connection
                await stream.write(resp)
                await self.close_stream(stream)
            except tornado.iostream.StreamClosedError:
                log.debug("Lost connection from %s", address)
                break

    async def close_stream(self, stream):
        """Gopher connections are closed by writing a . on a single line then
           closing the underlying transport."""
        await stream.write(gb.protocol.eof.encode("ascii"))
        await stream.write(gb.protocol.crlf.encode("ascii"))
        stream.close()


class ImplicitGopherServer(GopherServer):
    def __init__(self, path, magic):
        super().__init__()
        log.info("Starting ImplicitGopherServer with path %s", path)
        self.mode = gb.mode.ImplicitMode(path, magic)

    async def lookup(self, stream, data):
        return self.mode.lookup(data)


class ExplicitGopherServer(GopherServer):
    pass
