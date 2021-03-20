import re
import json
from bs4 import BeautifulSoup 
import requests, sys

# get
'''
url = "http://www.cntour.cn/"
strhtml = requests.get(url)
print(strhtml.text)
'''

# post
def get_translate_date(word = None):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    from_data={
        'i':word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16162336339382',
        'sign': '5ae37ba4c34bc07d61ee9251103f0e85',
        'lts': '1616233633938',
        'bv': 'a70166da0759fd61f4c3fd22f18d04e3',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
    }

    # 发起请求
    response = requests.post(url,data=from_data)
    # 解析为json,打印返回响应内容
    content = json.loads(response.text)
    print(content)
    # 打印翻译后内容
    # print(content['translateResult'][0][0]['tgt'])

# 作为脚本直接执行, import 到其他的 python 脚本中不被执行
if __name__ == '__main__':
    get_translate_date('我爱中国')


# BeautifulSoup解析工具
url = 'http://www.cntour.cn/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
strhtml = requests.get(url,headers=headers)
# strhtml = requests.get(url,proxies=proxies)
soup = BeautifulSoup(strhtml.text,'html')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(2) > a')
print(data)

# 清洗数据
for item in data:
    result = {
        'title':item.get_text(),
        'link':item.get('href'),
        'id':re.findall('\d+',item.get('href'))
    }
print(result)

'''
# 趴小说
targetUrl = 'http://www.biqukan.com/1_1094/5403177.html'
strhtml = requests.get(url=targetUrl)
print(strhtml.text)
# 解析HTML信息
htmlSoup = BeautifulSoup(strhtml.text,'html')
data = htmlSoup.find_all('div',class_='showtxt')
print(data[0].text.replace('\xa0'*8,'\n\n'))
'''

# 爬取整部小说
# -*- coding:UTF-8 -*-

"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2017-09-13
"""
class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])                                #剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2017-09-13
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2017-09-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载，共：%s个链接：' % dl.nums)
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%   %s/%s" % (float(i/dl.nums),i,dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')