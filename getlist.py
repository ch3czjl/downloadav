import requests,headers
# import threading
# import datetime
import os
import urllib3
def getlist(urlxuhao):
    url1 ='https://z.weilekangnet.com:59666/data7/91C8DAAE13BEEF8A/'+ urlxuhao +'/360p/360p.m3u8'
    headers_m3u8 = {
        'Host': 'z.weilekangnet.com:59666',
        'Connection': 'keep-alive',
        'Origin': 'https://www.bym6zv1e3485q896y0l134bag002.top:52789',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://www.bym6zv1e3485q896y0l134bag002.top:52789/static/player/dplayer.html?v=1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7',
    }
    headers = headers_m3u8
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url1,headers=headers,stream=True,verify=False,)
    # print(type(r.text))
    filename = 'indexhtml.m3u8'
    with open(filename, 'w') as file_object:
        file_object.write(r.text)
    text_list = []
    f = open(filename, 'r', encoding='utf-8')
    text_list = f.readlines()
    print('成功写入',text_list)
    return url1,filename