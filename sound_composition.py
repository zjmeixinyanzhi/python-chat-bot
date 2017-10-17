#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pydub import AudioSegment

def get_files(rootDir):
    files = []
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        files.append(path)
        if os.path.isdir(path): 
            Test2(path)
    return files

def do_composite(files):
    temp = files[0]
    print temp
    enPath = "%s%s/%s"%(enDir,file,enfile) 
    result =  AudioSegment.from_mp3(temp)
    result.export('D:/all.mp3', format="mp3")
    del files[0]
    for s in files:
        curr = AudioSegment.from_mp3(s)
        result = result + curr  
    result.export('D:/all.mp3', format="mp3")    



if __name__ == '__main__':

    sounds = get_files('D:/sound/')
    do_composite(sounds)
