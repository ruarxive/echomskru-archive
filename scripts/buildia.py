#!/usr/bin/env python
import csv
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from filehash import FileHash

DIRPATH = 'programs'


ia_headers = ["identifier", "file", "description", "subject[0]", "subject[1]", "subject[2]", "title", "creator", "date", "collection"]
def iameta(dirpath):
    dirs = os.listdir(dirpath)
    for d in dirs:
        if not os.path.isdir(os.path.join(dirpath, d)): continue
        f = open(os.path.join(DIRPATH, d, 'uploading.csv'), 'w', encoding='utf8')
        writer = csv.writer(f, delimiter=',')
        writer.writerow(ia_headers)

        files = os.listdir(os.path.join(dirpath, d))
        for fname in files:
            if fname == 'uploading.csv': continue
            fullname = os.path.join(dirpath, d, fname)
            row = ['echomskru-%s' %(d), fname,
                       'Echo of Moscow program %s' % (d),
                        'radio', 'echoofmoscow', 'echomskru', 'Echo of Moscow %s' % (d), '', '', 'opensource_audio']
            writer.writerow(row)

if __name__ == "__main__":
    iameta(DIRPATH)