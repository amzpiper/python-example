import requests
import json


class Test():
    def __init__(self):
        self.host = 'https://117.78.22.246:1443'
        self.service = '/dm_property_overview'
        self.X_HW_ID='Hi-bmsoft2021__io.yibei'
        self.X_HW_APPKEY='0eaEGdVF+DgpgKN5JlgJIw=='

    def get(self):
        url = self.host + self.service
        print("url:%s" % url)
        headers = {
            'X-HW-ID': self.X_HW_ID,
            'X-HW-APPKEY': self.X_HW_APPKEY
        }

        try:
            response = requests.get(url=url, headers=headers,verify=False)
            print("response:%s" % response.json())
        except Exception as e:
            response = {
                "error":"500"
            }
            print(response)

test = Test()
test.get()
