#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import bot_1, bot_2

if __name__ == '__main__':
    count = 0
    ss = raw_input('启动！输入第一句话：')
    for i in range(1,20):
        ss1 = bot_1.do_chat(ss)
        print '机器人A:',ss1
        ss = bot_2.do_chat(ss1)
        print '机器人B:',ss
        if ss1 == ss:
            count = count + 1
        if count == 3:
            print '俩二货已经聊死了~'
            break