#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pygame
import baidu_asr
import bot_1, bot_2

if __name__ == '__main__':
    count = 0
    pygame.mixer.init()
    print int(time.time())
    ss = raw_input('启动！输入第一句话：')
    for i in range(1,20):

        ss1 = bot_1.do_chat(ss)
        now = (time.time())
        print '机器人A:',ss1
        sound1 = 'D:/'+ str(now) +'A.mp3'
        baidu_asr.to_sound(ss1,sound1,1)
        
        track1 = pygame.mixer.music.load(sound1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == 1:
            time.sleep(0.5)
        

        ss = bot_2.do_chat(ss1)
        now = (time.time())
        print '机器人B:', ss

        sound2 = 'D:/' + str(now) + 'B.mp3'
        baidu_asr.to_sound(ss,sound2,0)
        track2 = pygame.mixer.music.load(sound2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == 1:
            time.sleep(0.5)

        if ss1 == ss:
            count = count + 1
        if count == 3:
            print '俩二货已经聊死了~'
            break
