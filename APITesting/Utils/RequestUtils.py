from requests_oauthlib import OAuth1
from APITesting.Utils.RequestInterface import Request


class RequestUtil(Request):

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used for get request (Get Data)
    param: url,statusCode
    return: Response
    '''
    def get(self,url,statusCode=None):
        actualUrl = self.endpoint+url
        auth = OAuth1(self.securityKey["key"],self.securityKey["secret"])
        response = self.request.get(url=actualUrl,auth=auth)
        if response.status_code == statusCode:
            return response
        else:
            print(f"Expected result:{statusCode} but actual result is {response.status_code}")
            return None

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used for post request (Create Data)
    param: url,payload,statusCode,header
    return: Response
    '''
    def post(self,url,payload=None,statusCode=None,header=None):
        actualUrl = self.endpoint+url
        auth = OAuth1(self.securityKey["key"],self.securityKey["secret"])
        if header==None:
            header = {"Content-Type":"application/json"}
        response = self.request.post(url=actualUrl,json=payload,headers=header,auth=auth)
        if response.status_code == statusCode:
            return response
        else:
            print(f"Expected result:{statusCode} but actual result is {response.status_code}")
            return None

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used for delete request (Delete Data)
    param: url,statusCode
    return: Response
    '''
    def delete(self,url,statusCode=None):
        actualUrl = self.endpoint+url
        auth = OAuth1(self.securityKey["key"],self.securityKey["secret"])
        response = self.request.delete(url=actualUrl,auth=auth)
        if response.status_code == statusCode:
            return response
        else:
            print(f"Expected result:{statusCode} but actual result is {response.status_code}")
            return None

    '''
    created By: Shivam Ojha
    since: 29 July 2024
    desc: This method is used for put request (Update Data)
    param: url,payload,statusCode,header
    return: Response
    '''
    def put(self,url,payload=None,statusCode=None,header=None):
        actualUrl = self.endpoint+url
        auth = OAuth1(self.securityKey["key"],self.securityKey["secret"])
        if header==None:
            header = {"Content-Type":"application/json"}
        response = self.request.put(url=actualUrl,json=payload,headers=header,auth=auth)
        if response.status_code == statusCode:
            return response
        else:
            print(f"Expected result:{statusCode} but actual result is {response.status_code}")
            return None