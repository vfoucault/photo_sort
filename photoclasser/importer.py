import re
from datetime import datetime
import os
import shutil
import piexif
import logging
from pprint import pprint
from conts import Const


class Importer:

    def __init__(self, photo, dst_path, format_out='%Y%m%d', move_file=False, create_dest=True):

        self.photo = photo
        self.full_dest_path = "%s/%s" % (dst_path, photo.date.strftime(format_out))
        self.dest_exists = os.path.exists(self.full_dest_path)
        self.move_file = move_file
        self.create_dest = create_dest


    def run(self):

        if self.create_dest and not self.dest_exists:
            os.mkdir(self.full_dest_path)
        if self.move_file:
            logging.info("Moving file %s into %s", self.photo.path, self.full_dest_path)
            shutil.move(self.photo.path, self.full_dest_path)
        else:
            logging.info("Copying file %s into %s", self.photo.path, self.full_dest_path)
            shutil.copy2(self.photo.path, self.full_dest_path)
