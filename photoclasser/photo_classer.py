import os
import shutil

from photoclasser.conts import Const
from photoclasser.photo import Photo, PhotoError
import logging


class PhotoClasser:

    def __init__(self, source_folder, import_to, create_folder, format_folder='%Y%m%d', mode='copy', create_dest=True):
        self.logger = logging.getLogger()
        self.source_folder = source_folder
        self.import_to = import_to
        self.create_folder = create_folder
        self.dest_format = format_folder
        self.is_dest_exists = os.path.exists(import_to)
        self.filelist = os.listdir(source_folder)
        self.imageslist = [image for image in self.filelist if Const.IMAGE_REGEX.match(image)]
        self.photos = [Photo("%s/%s" % (source_folder, photo)) for photo in self.imageslist]
        self.photo_count = len(self.photos)
        self.mode = mode
        self.create_dest = create_dest

    def run_importer(self):
        if not os.path.exists(self.import_to) and self.create_dest:
            self.logger.info('Creating destination path %s', self.import_to)
            os.mkdir(self.import_to)
        else:
            raise PhotoClasserError('import path does not exists and create_dest is false 8')

        for photo in self.photos:
            full_import_to = '%s/%s' % (self.import_to, photo.date.strftime(self.dest_format))
            if not os.path.exists(full_import_to):
                os.mkdir(full_import_to)
            if self.mode == 'copy':
                self.logger.info('* importing %s to %s', photo.filename, self.import_to)
                shutil.copy2(photo.path, full_import_to)


class PhotoClasserError(StandardError):
    pass