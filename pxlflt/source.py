import requests
from io import BytesIO
from PIL import Image


class HTTPImage():
    def __init__(self, url):
        self.url = url

    @property
    def _img_data(self):
        response = requests.get(self.url)
        response.raise_for_status()

        return BytesIO(response.content)

    def to_bitmap(self):
        with Image.open(self._img_data) as im:
            return im.resize((1280, 720)).load()
