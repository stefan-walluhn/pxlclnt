import asyncio
import click
import logging

from pxlflt.source import HTTPImage
from pxlflt.strategy import LinearStrategy


async def pixel_flut_client(host, port, pxls):
    reader, writer = await asyncio.open_connection(host, port)

    while True:
        logging.debug('start writing to socket')
        writer.write(pxls)
        logging.debug('wait for drained socket')
        await writer.drain()
        logging.debug('socket drained')

    writer.close()
    await writer.wait_closed()


@click.command()
@click.option('-h', '--host', default="pixelflut.uwu.industries")
@click.option('-p', '--port', type=click.IntRange(1, 65535), default=1234)
@click.option('-u', '--url')
def run_client(host, port, url):
    logging.basicConfig(level=logging.DEBUG)

    strategy = LinearStrategy(HTTPImage(url).to_bitmap())
    pxls = strategy.pxlsarray

    asyncio.run(pixel_flut_client(host, port, pxls))


if __name__ == '__main__':
    run_client()
