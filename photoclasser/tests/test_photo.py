import unittest
from pprint import pprint
import os

import shutil
from hamcrest import *
from datetime import datetime
from photoclasser.photo import Photo, PhotoError
from photoclasser.photo_classer import PhotoClasser

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


class PhotoClasserTester(unittest.TestCase):

    def setUp(self):
        if os.path.exists('photoclasser/tests/resources/destfolder'):
            shutil.rmtree('photoclasser/tests/resources/destfolder')


    def test_classer_init(self):

        # Given

        # When
        classer = PhotoClasser('photoclasser/tests/resources/folder1', import_to='photoclasser/test/resources/destfolder',
                               create_folder=True, format_folder='%Y%m%d')

        # Then
        assert_that(classer.photo_count, is_(3))
        assert_that(classer.is_dest_exists, is_(False))
        assert_that(classer.photos[0], is_(instance_of(Photo)))


    def test_classer_copy(self):
        # Given
        classer = PhotoClasser('photoclasser/tests/resources/folder1', import_to='photoclasser/tests/resources/destfolder',
                               create_folder=True, format_folder='%Y%m%d')

        # When
        classer.run_importer()

        # Then
        assert_that(os.path.exists('photoclasser/tests/resources/destfolder'), is_(True))
        assert_that(os.path.exists('photoclasser/tests/resources/destfolder/20170115'), is_(True))
        assert_that(os.path.exists('photoclasser/tests/resources/destfolder/20170115/20170115_155700.jpg'), is_(True))
        assert_that(os.path.exists('photoclasser/tests/resources/destfolder/20170108'), is_(True))
        assert_that(os.path.exists('photoclasser/tests/resources/destfolder/20170108/20170108_172851.jpg'), is_(True))


