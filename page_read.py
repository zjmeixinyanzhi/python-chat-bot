#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import baidu_asr
import sound_composition
import pygame

def get_content():
    page_url = 'http://www.zreading.cn/archives/6086.html'
    driver = webdriver.PhantomJS()
    driver.get(page_url)
    dom = driver.page_source
    soup = BeautifulSoup(dom, 'lxml')
    content = []
    # 提取标题
    content.append(soup.h2.text)
    # 提取文章内容
    p_list = soup.find_all('p')
    for p in p_list:
        content.append(p.text)
        if p.text.startswith(u'左岸记'):
            break
    return content

if __name__ == '__main__':
    content = get_content()
    # 文字转语音
    for p in content:
        now = time.time()
        baidu_asr.to_sound(p,'D:/sound/'+ str(now) +'.mp3',1)
    # 合并声音片段
    sounds = sound_composition.get_files('D:/sound/')
    sound_composition.do_composite(sounds,'D:/all.mp3')
    # 朗读
    pygame.mixer.init()
    track = pygame.mixer.music.load('D:/all.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == 1:
        time.sleep(0.5)