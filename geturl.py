#coding=utf8

import requests,headers,urldizhi
# import threading
# import datetime
import os
import urllib3

def geturl(url2):
    headers_page = {

        'Host': 'www.bym6zv1e3485q896y0l134bag002.top:52789',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': urldizhi.urldizhi,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7',
        'Cookie': 'UM_distinctid=17413c6081b533-06bb57cf05248-54133110-1fa400-17413c6081c6eb; CNZZDATA1274570257=2090638710-1598059189-null%7C1598059189; Hm_lvt_07f2c7e5bd9592209d606f0184fc3d8f=1598059580,1598059739; Hm_lpvt_07f2c7e5bd9592209d606f0184fc3d8f=1598059779; recente=%5B%7B%22vod_name%22%3A%22%E9%85%92%E5%90%A7%E5%A4%A7%E5%A5%B6DJ%E6%80%A7%E6%84%9F%E7%BE%8E%E5%A5%B3%22%2C%22vod_url%22%3A%22https%3A%2F%2Fwww.bym6zv1e3485q896y0l134bag002.top%3A52789%2Findex.php%2Fvod%2Fplay%2Fid%2F125103%2Fsid%2F1%2Fnid%2F1.html%22%2C%22vod_part%22%3A%22%E7%AC%AC1%E9%9B%86%22%7D%5D',
    }

    headers = headers_page
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url2,headers=headers,stream=True,verify=False,)
    # print(type(r.text),r.text)
    filename = 'indexhtml.m3u8'
    with open(filename, 'w') as file_object:
        file_object.write(r.text)
    text_list = []
    f = open('indexhtml.m3u8', 'r')
    text_list = f.read()
    # print(len(text_list))
    def find_repeat(source,elmt): # The source may be a list or string.
        elmt_index=[]
        s_index = 0;e_index = len(source)
        while(s_index < e_index):
            try:
                temp = source.index(elmt,s_index,e_index)
                elmt_index.append(temp)
                s_index = temp + 1
            except ValueError:
                break
        return elmt_index
    x = find_repeat(text_list,'jpg')
    title_str = find_repeat(text_list,'title=')
    # print(type(title_str),len(title_str),title_str[0],title_str)
    # print(type(x),len(x),x[0],x)
    jpg_list = []
    # print(text_list[x[0]-17])
    # print(text_list[x[0]])
    for i in x:
        # print(text_list[i])
        jpg_str = ''
        for k in range(17,1,-1):
            # print(k,text_list[i-k],type(k))
            jpg_str = jpg_str + text_list[i-k]
            # print(jpg_str)
        jpg_list.append(jpg_str)
    # print(jpg_list)

    title_list = []
    for o in title_str:
        # print(text_list[o+7])
        title_str_str = ''
        for p in range(0,15):
            # print(p,text_list[o+7+p],type(p))
            title_str_str = title_str_str + text_list[o+7+p]
            # print(title_str_str)
        title_list.append(title_str_str)
    # print(jpg_list)
    # print(title_list)
    title_list_dan = []
    for q in range(0,len(title_list),2):
        # print(title_list[q])
        title_list_dan.append(title_list[q])
    # print(title_list_dan)

    # return jpg_list,title_list
    # print(jpg_list,title_list_dan)
    return jpg_list,title_list_dan

url2 = urldizhi.urldizhi
x = geturl(url2)[0]
y = geturl(url2)[1]
# print(x[0],type(x[0]))
print(x)
print(y)




