import requests



def getm3u8(url,headers):
    url2 = url + '360p.m3u8'
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url2,headers=headers,stream=True,verify=False,)
    # print(type(r.text),r.text)
    filename = 'index.m3u8'
    with open(filename, 'w') as file_object:
        file_object.write(r.text)
    text_list = []
    f = open('index.m3u8', 'r')
    text_list = f.read()
    print(text_list)
    return url2

