import os
from urllib.request import urlopen, Request

from django.conf import settings


class DataSource:

    def __init__(self, store_config):
        self.name = store_config['name']
        self.url = store_config['data_source']['url']
        self.type = store_config['data_source']['type']

    @staticmethod
    def get_all_subclasses():
        """
        Returns all subclasses, not only direct subclasses, but also
        all subclasses of subclasses, and so on.
        """
        subclasses = {}

        def get_subclasses(subclasses, cls):
            subclasses[cls.__name__] = cls
            for subclass in cls.__subclasses__():
                get_subclasses(subclasses, subclass)

        get_subclasses(subclasses, DataSource)

        return subclasses

    def fetch(self):
        pass


class XmlDataSource(DataSource):

    def fetch(self, url=None, filename=None, headers=None):
        print('fetch files for {}'.format(self.name))

        url = url or self.url
        filename = filename or '{}.xml'.format(self.name.lower())
        filepath = os.path.join(settings.ST_STORES_DATA_DIR, filename)

        request = Request(url, headers=headers or {})
        response = urlopen(request)

        chunk_size = 16 * 1024

        with open(filepath, 'wb') as f:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break

                f.write(chunk)

        return filename