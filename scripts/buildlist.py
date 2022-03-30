#!/usr/bin/env python
import csv
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from filehash import FileHash

DIRPATH = 'programs'
URLPAT = 'https://f001.backblazeb2.com/file/IKPUBLIC/webcollect2022/echomskru2022/media/programs/%s/%s'

def run():
    alist = os.listdir(DIRPATH) 
    print('program_key,fileurl')
    for d in alist:
        if not os.path.isdir((os.path.join(DIRPATH, d))): continue
        files = os.listdir(os.path.join(DIRPATH, d))
        for f in files:
            print('%s,%s' % (d, URLPAT % (d, f)))

if __name__ == "__main__":
    run()