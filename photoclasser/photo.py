from datetime import datetime
import os
import piexif
import logging
from pprint import pprint


class PhotoError(StandardError):
    pass


class Photo:

    def __init__(self, path):
        self.path = path
        self.filename = self.path.split("/")[-1]
        if os.path.exists(self.path):
            self.exif_data = piexif.load(path)
            self.date = datetime.strptime(self.exif_data['0th'][306], "%Y:%m:%d %H:%M:%S")
        else:
            logging.error('file path %s does not exists or not readable !', self.path)
            raise PhotoError('File not found')

