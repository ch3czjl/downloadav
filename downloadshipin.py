"""
@author :Eric-chen
@contact :sygcrjgx@163.com
@time :2019/6/16 15:32
@desc :
"""
import requests
import threading
import datetime
import os
import getlist
import geturl
import urllib3
import hebing_ts

count = 0;


def Handler(start, end, url, filename):
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

    for i in filename[start:end]:
        global count
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url + i.replace("\n",""),
                         headers=headers,
                         stream=True,
                         verify=False,)

        with open("C:\\python\\zhangjl\\downloadshipin\\" + i.replace("\n", ""), "wb") as code:
            code.write(r.content)
        count = count + 1
        print("下载进度：%.2f" % (count / len(filename)))


def download_file(url,name,num_thread=100):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print("------------------------current working directory------------------" + cwd)
    f = open(filename, 'r', encoding='utf-8')
    text_list = f.readlines()
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


    # print('s_list',s_list)

    f.close()
    file_size = len(s_list)

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': s_list})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

    cmd = hebing_ts.before_merge(name)



# def before_merge():
#     cwd = os.getcwd()  # 获取当前目录即dir目录下
#     print("------------------------current working directory------------------" + cwd)
#     f = open('index.m3u8', 'r', encoding='utf-8')
#     text_list = f.readlines()
#     print(text_list)
#     files = []
#     for i in text_list:
#         if i.find('#EX') == -1:
#             files.append(i)
#     f.close()
#     tmp = []
#     for file in files[0:568]:
#         tmp.append(file.replace("\n", ""))
#         # 合并ts文件
#     # os.chdir("ts/")
#     shell_str = '+'.join(tmp)
#     # print(shell_str)
#     shell_str = 'copy /b ' + shell_str + str(geturl.geturl(url2)[1])+ ' 5.mp4' + '\n' + 'del *.ts'
#     return shell_str
#
#
# def wite_to_file(cmdString):
#     cwd = os.getcwd()  # 获取当前目录即dir目录下
#     print("------------------------current working directory------------------" + cwd)
#     f = open("combined.cmd", 'w')
#     f.write(cmdString)
#     f.close()


if __name__ == '__main__':
    url2 = 'https://www.bytpcl6w9j0w9ku52o.fun:52789/index.php/vod/type/id/1/page/3.html'
    x = geturl.geturl(url2)

    for i in x:
        u = getlist.getlist(i[0])
        url = u[:-9]
        namepian = i[1][:-8] + '.mp4'
        print(i[0],i[1])
        # print(url)
        # print(namepian)
    # url = "https://ef6of2321ojq3ke2e1qjjk72eehebwt6.weilekangnet.com:59666/data7/555E29C8F0224EDF/6321A3B0458BA0E3/360p/";
    # 下载：开始下载
        start = datetime.datetime.now().replace(microsecond=0)
        download_file(url,namepian)
        end = datetime.datetime.now().replace(microsecond=0)
        print(end - start)
    # 结束下载
    # 合并小文件
    #     cmd = before_merge();
    # # 把合并命令写到文件中
    #     wite_to_file(cmd);
