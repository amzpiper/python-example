import re
import requests
import json
from bs4 import BeautifulSoup 

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