#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json
github_url = 'http://www.tuling123.com/openapi/api'

def do_chat(word):
    data = json.dumps({'key':'XXXXXXXXXXXXXXXXXXXXXXXXX', 'info':word})
    r = requests.post(github_url, data, headers={'Accept': 'application/json'})
    return r.json()['text']

if __name__ == '__main__':
    print do_chat('今天星期几？')