#!/usr/bin/env python
import csv
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from filehash import FileHash

DIRPATH = 'lists'


def run():
    alist = os.listdir(DIRPATH) 
    print('key,name')
    for a in alist:
        print(a.rsplit('.', 1)[0] + ',' + '' )

if __name__ == "__main__":
    run()