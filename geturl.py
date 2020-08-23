#coding=utf8

import requests,daili
# import threading
# import datetime
import os
import urllib3

def geturl(url2,headers_page):


    headers = headers_page
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url2,headers=headers,stream=True,verify=False,)
    # print(type(r.text),r.text)
    filename = 'yemian.m3u8'
    with open(filename, 'w') as file_object:
        file_object.write(r.text)
    text_list = []
    f = open('yemian.m3u8', 'r')
    text_list = f.read()
    # print(text_list)
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

    for jishu in range(len(jpg_list)):
        if jishu % 2 == 0:
            del jpg_list[0]
        else:
            jpg_list.append(jpg_list[0])
            del jpg_list[0]

    return jpg_list,title_list_dan

url2 = daili.url_yemian
headers_page = daili.headers_page
x = geturl(url2,headers_page)[0]
y = geturl(url2,headers_page)[1]
# print(x[0],type(x[0]))
print(x)
print(y)




