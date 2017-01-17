import unittest
from pprint import pprint

from hamcrest import *
from datetime import datetime
from photoclasser.photo import Photo, PhotoError
from photoclasser.importer import Importer

from mock import mock, patch

class PhotoTester(unittest.TestCase):

    def test_photo_object(self):
        # Given
        # When
        photo = Photo('photoclasser/tests/resources/folder1/20170115_155700.jpg')

        # Then
        assert_that(photo.date, is_(datetime(2017, 01, 15, 15, 56, 59)))

    def test_photo_not_exists(self):
        # Given

        # When
        # Then
        with self.assertRaises(PhotoError):
            Photo('not_existing_photo')


class ImporterTester(unittest.TestCase):

    def test_importer_init(self):

        # Given
        photo = Photo('photoclasser/tests/resources/folder1/20170115_155700.jpg')

        # When
        importer = Importer(photo, '/somewhere', format_out='%Y%m%d', create_dest=True, move_file=False)

        # Then
        assert_that(importer.full_dest_path, is_('/somewhere/20170115'))
        assert_that(importer.dest_exists, is_(False))

    @patch('os.mkdir')
    @patch('shutil.copy2')
    def test_importer_init(self, mock_os_mkdir, mock_copy2):
        # Given
        mock_os_mkdir.returnvalue = True
        mock_copy2.returnvalue = True
        toto = mock.MagicMock()
        toto.method_calls
        photo = Photo('photoclasser/tests/resources/folder1/20170115_155700.jpg')
        importer = Importer(photo, '/somewhere', format_out='%Y%m%d', create_dest=True, move_file=False)

        # When
        importer.run()

        # Then
        pprint(mock_copy2.method_calls)
        pprint(mock_os_mkdir.methos_calls)



