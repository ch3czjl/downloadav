import getlist,geturl,daili,downloadshipin_dange,hebing_ts,getm3u8,datetime

url_yemian = daili.url_yemian

headers_page = daili.headers_page
headers_m3u8 = daili.headers_m3u8
x = geturl.geturl(url_yemian,headers_page)
print('x[0]:', x[0])
print('x[1]:', x[1])

for xuhao in range(0,len(x[0])):
    url_dangeshipin = getlist.get_xiazai_url(x[0][xuhao])
    getm3u8.getm3u8(url_dangeshipin,headers_m3u8)
    start = datetime.datetime.now().replace(microsecond=0)

    downloadshipin_dange.download_file(url_dangeshipin)

    end = datetime.datetime.now().replace(microsecond=0)
    print(end - start)
    # print('kaishihebing')
    print('xuhao[1][xuhao]:',x[1][xuhao])
    hebing_ts.before_merge(x[1][xuhao])
