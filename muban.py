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

count = 0;


def Handler(start, end, url, filename):
    headers = {
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
    for i in filename[start:end]:
        global count

        r = requests.get("z.weilekangnet.com:59666" + i.replace("\n", ""),
                         headers=headers,
                         stream=True)

        with open("C:\\python\\zhangjl\\downloadav\\" + i.replace("\n", ""), "wb") as code:
            code.write(r.content)
        count = count + 1
        print("下载进度：%.2f" % (count / len(filename)))


def download_file(url, num_thread=100):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print("------------------------current working directory------------------" + cwd)
    f = open('indexhtml.m3u8', 'r', encoding='GBK')
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


def before_merge():
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print("------------------------current working directory------------------" + cwd)
    f = open('indexhtml.m3u8', 'r', encoding='GBK')
    text_list = f.readlines()
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
    shell_str = 'copy /b ' + shell_str + ' 5.mp4' + '\n' + 'del *.ts'
    return shell_str


def wite_to_file(cmdString):
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print("------------------------current working directory------------------" + cwd)
    f = open("combined.cmd", 'w')
    f.write(cmdString)
    f.close()


if __name__ == '__main__':
    url = "z.weilekangnet.com:59666";
    # 下载：开始下载
    start = datetime.datetime.now().replace(microsecond=0)
    download_file(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print(end - start)
    # 结束下载
    # 合并小文件
    cmd = before_merge();
    # 把合并命令写到文件中
    wite_to_file(cmd);
