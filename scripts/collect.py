#!/usr/bin/env python
import csv
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from filehash import FileHash

FILEPATH = 'echomskru_mp3/urls.csv'
DIRPATH = 'echomskru_mp3'

def run():
    reader = csv.reader(open(FILEPATH, 'r', encoding='utf8'))
    for row in reader:
        if len(row) == 0: continue
        filename = row[0].rsplit('/', 1)[-1]
        fullp = os.path.join(DIRPATH, filename)
        if not os.path.exists(fullp):
            print(row[0])

if __name__ == "__main__":
    run()