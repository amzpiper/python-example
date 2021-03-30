import requests
import json

DNS_DRIVER = None


class dns_zone_driver():

    def __init__(self):
        self.host = 'https://www.baidu.com'
        self.port = 20120
        self.view_id = "default"
        self.auth_name = "admin"
        self.auth_pw = "zdns"

    @classmethod
    def get_instance(cls):
        global DNS_DRIVER
        if not DNS_DRIVER:
            DNS_DRIVER = cls()
        return DNS_DRIVER

    def get_acls_driver(self):
        url = (self.host + ":" + str(self.port) + '/acls')
        print("all acls :%s" % url)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        try:
            response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        except Exception as e:
            response = {
                "error":"500"
            }
            print(response)
            return response

        print("all acls response:%s" % response.json())
        return json.loads(response.json())

    def get_acl_one_driver(self,id):
        url = (self.host + ":" + str(self.port) + '/acls/' + id)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)
        print("one of acls :%s" % url)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("one of acls response:%s" % response.json())

        return json.loads(response.json())

    def get_views_driver(self):
        url = (self.host + ":" + str(self.port) + '/views')
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)

        print("all views :%s" % url)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("all views response:%s" % response.json())

        return json.loads(response.json())

    def get_view_one_driver(self,id):
        url = (self.host + ":" + str(self.port) + '/views/' + id)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)

        print("one of view :%s" % url)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("one of view response:%s" % response.json())

        return json.loads(response.json())

    def get_zones_driver(self, view_id=None):
        """   view all zone     """
        self.view_id = view_id
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones')
        print("view all zone :" + url)
        params = {'current_user': 'admin'}
        auth = (self.auth_name, self.auth_pw)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        data = json.dumps(params)

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("view all zone response:%s" % response.json())

        return json.loads(response.json())

    def get_zone_one_driver(self, view_id, zone_id):
        """   view one zone     """
        self.view_id = view_id
        
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones/' + zone_id)
        print("view one zone :%s" % url)
        data = {}
        data["current_user"] = 'admin'
        data["need_zone_content"] = 'yes'
        data = json.dumps(data)
        auth = (self.auth_name, self.auth_pw)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("view one zone response:%s" % response.json())

        return json.loads(response.json())

    def get_rrs_driver(self,view_id, zone_id):
        self.view_id = view_id

        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones/' + zone_id + "/rrs")
        print("view all rrs :" + url)
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("view all rrs response:%s" % response.json())

        return json.loads(response.json())
    
    def get_rrs_one_driver(self,view_id, zone_id,rrs_id):
        """   view one rrs     """
        self.view_id = view_id
        url = (self.host + ":" + str(self.port) +
               '/views/' + self.view_id + '/zones/' + zone_id + "/rrs")
        print("view all rrs :%s" % url)
        auth = (self.auth_name, self.auth_pw)
        params = {'current_user': 'admin'}
        data = json.dumps(params)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        response = requests.get(url, data=data,headers=headers,auth=auth, verify=False)
        print("view all rrs response:%s" % response.json())

        rrsDict = json.loads(response.json())
        rrsList = rrsDict["resource"]
        rrs = {
            "error":"None"
        }
        for rrsItem in rrsList:
            if rrsItem['name'] == rrs_id:
                print("view all rrs response:%s" % response.json())
                rrs = rrsItem

        return rrs