import requests
# import threading
# import datetime
import os
import urllib3
def getlist(urlxuhao):
    url1 ='https://ef6of2321ojq3ke2e1qjjk72eehebwt6.weilekangnet.com:59666/data7/555E29C8F0224EDF/'+ urlxuhao +'/360p/360p.m3u8'

    headers = {'Host': 'ef6of2321ojq3ke2e1qjjk72eehebwt6.weilekangnet.com:59666',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept': '*/*',
    'Origin': 'https://www.bytpcl6w9j0w9ku52o.fun:52789',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7',
    }
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url1,headers=headers,stream=True,verify=False,)
    # print(type(r.text))
    filename = urlxuhao + 'index.m3u8'
    with open(filename, 'w') as file_object:
        file_object.write(r.text)
    text_list = []
    f = open(urlxuhao + 'index.m3u8', 'r', encoding='utf-8')
    text_list = f.readlines()
    print('成功写入',text_list)
    return url1,filename