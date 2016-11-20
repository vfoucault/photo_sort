from PhotoClasser import PhotoClasser


class PhotoClasserBuilder:

    def __init__(self):
        self.obj_photo_classer = None
        self.src_directory = None
        self.dst_directory = None
        self.move_files = None

    def with_srcdir(self, directory):
        self.src_directory = directory
        return self

    def with_dstdir(self, directory):
        self.dst_directory = directory
        return self

    def with_move(self, boolean):
        self.move_files = boolean
        return self

    def build(self):
        myobj = PhotoClasser(sourcedir=self.src_directory, targetdir=self.dst_directory)
        if self.move_files:
            myobj.move_files = True
        return myobj


