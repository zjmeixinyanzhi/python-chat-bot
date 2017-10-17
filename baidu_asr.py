#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from aip import AipSpeech

APP_ID = '10244407'
API_KEY = 'eRbQtT8ACHxDWzePjrpLfh71'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def to_word(sound):
    result_str = aipSpeech.asr(get_file_content(sound), 'pcm', 16000, {
        'lan': 'zh',
    })
    if result_str.has_key('result'):
        out_txt = result_str['result'][0]
    else:
        out_txt = "Null"
    return out_txt

# 转为语音
def to_sound(word,sound_path,per):
    result = aipSpeech.synthesis(word, 'zh', 1, {
        'vol': 5,
        'per': per,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(sound_path, 'wb') as f:
            f.write(result)
    #print dict

if __name__ == '__main__':

    to_sound('你好吗？','hello.mp3')