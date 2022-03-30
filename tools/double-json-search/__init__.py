import requests
import json


class Test():
    def __init__(self):
        self.host = 'https://111.203.142.107:1443'
        self.service = '/dm_person_details?start=2022-01-25 11:02:18&end=2022-01-25 11:19:18'
        self.X_HW_ID='sctest1001__shangguan'
        self.X_HW_APPKEY='CbbbaH2p3LTilp9+5jOdXg=='

    def get(self):
        url = self.host + self.service
        print("url:%s" % url)

        headers = {
            'X-HW-ID': self.X_HW_ID,
            'X-HW-APPKEY': self.X_HW_APPKEY
        }
        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.get(url=url, headers=headers,verify=False)
            print("response:%s" % json.loads(response.text))
            # 测试是否
            result = response.json().get('retJSON').get('result')
            print("result:%s" % result)
            for item in result:
                print("item.person_phone:%s" % item['person_phone'])
                
        except Exception as e:
            response = {
                "error":"500"
            }
            print(response)

test = Test()
test.get()
