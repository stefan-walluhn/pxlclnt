import io
from functools import lru_cache


class LinearStrategy():
    def __init__(self, bitmap):
        self.bitmap = bitmap

    def pxls(self):
        for y in range(720):
            for x in range(1280):
                yield self._to_px(x, y)

    @lru_cache(maxsize=None)
    def _to_px(self, x, y):
        r, g, b = self.bitmap[x, y]

        return f'PX {x} {y} {r:02x}{g:02x}{b:02x}\n'.encode() 

    @property
    def pxlsarray(self):
        sep = bytearray()
        return sep.join(self.pxls())
