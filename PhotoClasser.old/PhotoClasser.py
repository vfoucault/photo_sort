import os
import glob
import pprint
from datetime import datetime
import shutil
import logging


class PhotoClasser():

    def __init__(self, sourcedir, targetdir):
        self.srcdir = sourcedir
        self.targetdir = targetdir
        self.files = None
        self.dictdest = {}
        self.logger = logging.getLogger('myapp')
        hdlr = logging.FileHandler('photocopy.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(hdlr)
        self.logger.addHandler(ch)
        self.logger.info("Init photo classer")


    def get_files_in_src(self):
        files = glob.glob("%s/*" % self.srcdir)
        self.files = files

    def arrange_file_by_dest(self):
        for fname in self.files:
            fstat = os.stat(fname)
            dateobj = datetime.fromtimestamp(fstat.st_ctime)
            year = dateobj.strftime("%Y")
            strdate = dateobj.strftime("%Y-%m-%d")
            if not year in self.dictdest:
                self.dictdest[year] = {}
            if not strdate in self.dictdest[year]:
                self.dictdest[year][strdate] = []
            self.dictdest[year][strdate].append(fname)

    def create_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            self.logger.info("Creating the %s folder", directory)

    def create_dirs_alls(self):
        years = [ x for x in self.dictdest ]
        for year in years:
            if not os.path.exists("%s/%s" % (self.targetdir, year)):
                os.makedirs("%s/%s" % (self.targetdir, year))
            for datedir in self.dictdest[year]:
                if not os.path.exists("%s/%s/%s" % (self.targetdir, year, datedir)):
                    os.makedirs("%s/%s/%s" % (self.targetdir, year, datedir))

    def copy_files(self):
        for year in self.dictdest:
            for strdate, fnames in self.dictdest[year].items():
                destdir = "%s/%s/%s" % (self.targetdir, year, strdate)
                self.create_dir(destdir)
                for fname in fnames:
                    if os.path.exists("%s/%s" % (destdir, fname.split("/")[-1])):
                        ofilestat = os.stat(fname)
                        nfilestat = os.stat("%s/%s" % (destdir, fname.split("/")[-1]))
                        if ofilestat.st_ctime == nfilestat.st_ctime and ofilestat.st_size == nfilestat.st_size:
                            self.logger.error("File %s already exists. not copying it", fname.split("/")[-1])
                        else:
                            ext = fname.split("/")[-1][-4::]
                            nfname = "%s_001%s" % (fname.split("/")[-1][0:-4],ext)
                            self.logger.error("A file with the same filename exists. New fileanme : %s" % nfname)
                            self.logger.info("Copyinfo %s to %s", nfname, destdir)
                            shutil.copy2(fname, "%s/%s" % (destdir, nfname))
                    else:
                        self.logger.info("Copyinfo %s to %s", fname.split("\\")[-1], destdir)
                        shutil.move(fname, "%s/" % destdir)
                        #shutil.copy2(fname, "%s\\" % destdir)
                        #os.utime("%s\\%s" % (destdir, fname.split("\\")[-1]), (os.stat(fname).st_atime, os.stat(fname).st_mtime))
                        #shutil.copystat(fname, "%s\\%s" % (destdir, fname.split("\\")[-1]))



    def process(self):
        self.get_files_in_src()
        self.arrange_file_by_dest()
        self.copy_files()




