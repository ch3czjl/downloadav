"""
@author :Eric-chen
@contact :sygcrjgx@163.com
@time :2019/6/16 15:32
@desc :
"""
# -- coding: utf-8 --


import os




def before_merge(name):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print("------------------------current working directory------------------" + cwd)
    f = open('index.m3u8', 'r', encoding='utf-8')
    text_list = f.readlines()
    # print(type(text_list),text_list)
    ss_list = []
    sss_list = []
    s_list = []
    # print(len(text_list),type(text_list),text_list)
    for i in text_list:
        # print(i,type(i))
        if i.find('#EXTINF') == -1:
            # print(i)
            ss_list.append(i)
            # print(s_list)
    # print(ss_list)
    for j in ss_list:
        # print('j',type(j),j)
        if j.find('0out360p')!= -1:
            # j.replace(''''\n''','')
            # print('quchu',j)
            sss_list.append(j)
    # s_list = sss_list.replace('\n','')
    for k in sss_list:
        # print('k',k,type(k))
        k.strip()
        s_list.append(k)
    # print('s_list:',s_list)
    f.close()
    tmp = []
    for file in s_list:
        tmp.append(file.replace("\n", ""))
        # 合并ts文件
    # os.chdir("0out360p")
    # print('tmp:',tmp)
    shell_str = '+'.join(tmp)
    # print(shell_str)
    shell_str = 'copy /b ' + shell_str + ' ' + name + '.mp4'
    shell_str2 = 'del *.ts'
    # print('shell_str:',shell_str)
    os.system(shell_str)
    os.system(shell_str2)
    return shell_str


def wite_to_file(cmdString):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    # print("------------------------current working directory------------------" + cwd)
    f = open((x + ".cmd"), 'w')
    f.write(cmdString)
    f.close()


cmd = before_merge('asdfasdf')


