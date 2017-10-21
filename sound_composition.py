#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pydub import AudioSegment

AudioSegment.converter = "D:/ffmpeg.exe"
def get_files(rootDir):
    files = []
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        files.append(path)
        if os.path.isdir(path): 
            (path)
    return files

def do_composite(files, target_file):
    temp = files[0]
    print temp
    result = AudioSegment.from_mp3(temp)
    result.export(target_file, format="mp3")
    del files[0]
    for s in files:
        curr = AudioSegment.from_mp3(s)
        result = result + curr  
        result.export('D:/all.mp3', format="mp3")
        print s

if __name__ == '__main__':
    sounds = get_files('D:/sound/')
    do_composite(sounds,'D:/all.mp3')
