"""
@author :Eric-chen
@contact :sygcrjgx@163.com
@time :2019/6/16 15:32
@desc :
"""
# -*- coding:utf-8 -*-

import requests
import threading
import datetime
import os
import getlist
import geturl
import urllib3

count = 0;
import geturl,getlist,downloadshipin

def before_merge(name):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    # print("------------------------current working directory------------------" + cwd)
    f = open('indexhtml.m3u8', 'r', encoding='GBK')
    text_list = f.readlines()
    # print(text_list)
    files = []
    for i in text_list:
        if i.find('#EX') == -1:
            files.append(i)
    f.close()
    tmp = []
    for file in files[0:568]:
        tmp.append(file.replace("\n", ""))
        # 合并ts文件
    # os.chdir("ts/")
    shell_str = '+'.join(tmp)
    # print(shell_str)
    shell_str = 'copy /b ' + shell_str + ' ' + name + '\n' + 'del *.ts'
    os.system(shell_str)
    return shell_str


def wite_to_file(cmdString):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    # print("------------------------current working directory------------------" + cwd)
    f = open((x + ".cmd"), 'w')
    f.write(cmdString)
    f.close()

url2 = 'https://www.bytpcl6w9j0w9ku52o.fun:52789/index.php/vod/type/id/1/page/3.html'
name = geturl.geturl(url2)[1][0] + '.mp4'
# print(type(name),name)
cmd = before_merge(name)
# 把合并命令写到文件中
# wite_to_file(cmd)

