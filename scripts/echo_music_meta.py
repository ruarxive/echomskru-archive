#!/usr/bin/env python
import csv
import sys
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from filehash import FileHash
import shutil

headers = ['album', 'title', 'artist', 'year', 'length_seconds', 'filesize', 'sha256', 'filename']
def run(dirpath):
    hasher = FileHash('sha256')
    print(';'.join(headers))
    files = os.listdir(dirpath)
    for fname in files:
        fullname = os.path.join(dirpath, fname)
        try: 
            audio = MP3(fullname, ID3=EasyID3)
            row = [audio['album'][0], audio['title'][0], audio['artist'][0], audio['date'][0], str(audio.info.length), str(os.stat(fullname)[6]), hasher.hash_file(fullname), fname]
        except:
            continue
        print(';'.join(row))

ia_headers = ["identifier", "file", "description", "subject[0]", "subject[1]", "subject[2]", "title", "creator", "date", "collection"]
def iameta(dirpath):
    f = open('ruarxive_echomskru_media.csv', 'w', encoding='utf8')
    writer = csv.writer(f, delimiter=',')
    writer.writerow(ia_headers)
    files = os.listdir(dirpath)
    for fname in files:
        fullname = os.path.join(dirpath, fname)
        try: 
            audio = MP3(fullname, ID3=EasyID3)
            row = [fname.replace('.', '_'), fname,
                   'Record of the Echo Moskvy radio station     ' + audio['date'][0] + " " + audio['title'][0].replace(',', ' '),
                    'radio', 'Echo Moskvy', 'echomskru', audio['title'][0].replace(',', ' '), 'ruarxive', audio['date'][0], 'ruarxive-echomskru-media']
        except:
            continue
        writer.writerow(row)


def splitby(filename):
    f = open(filename, 'r', encoding='utf8')
    n = 0
    categories = {}
    for l in f:
        l = l.strip()
        n += 1
        if n == 1: continue
        filename = l.rsplit('/', 1)[-1]
        parts = filename.split('-')
        if len(parts) > 4:
            category = parts[3]
            if category not in categories.keys():
                categories[category] = []
            categories[category].append(l)
    for category in categories.keys():
        f = open(category + '.list', 'w', encoding='utf8')
        for l in categories[category]:
            f.write(l + '\n')
        f.close()

def reorganize(filename):
    f = open(filename, 'r', encoding='utf8')
    n = 0
    categories = {}
    for l in f:
        l = l.strip()
        n += 1
        if n == 1: continue
        filename = l.rsplit('/', 1)[-1]
        parts = filename.split('-')
        if len(parts) > 4:
            category = parts[3]
            if category not in categories.keys():
                categories[category] = []
            categories[category].append(l)
    for category in categories.keys():
        os.makedirs('programs/%s' % (category), exist_ok=True)
        for l in categories[category]:
            filename = l.rsplit('/', 1)[-1]
            if os.path.exists('echomskru_mp3/%s' % (filename)):
                shutil.move('echomskru_mp3/%s' % (filename), 'programs/%s/%s' % (category, filename))
                print('Move %s' % (filename))
            if os.path.exists('echomskru_mp3/%s.aria2' % (filename)):
                shutil.move('echomskru_mp3/%s.aria2' % (filename), 'programs/%s/%s.aria2' % (category, filename))
                print('Move %s' % (filename))


if __name__ == "__main__":
#    run(sys.argv[1])
#    splitby('echomskru_mp3/urls.csv')
#    iameta(sys.argv[1])
#    reorganize('echomskru_mp3/urls.csv')
