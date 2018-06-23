import json
import logging as log
from urllib.request import Request,urlopen,base64
from urllib.error import HTTPError
'''url="aquacrmsoftware.atlassian.net"
username="priyank@aquacrmsoftware.com"
token="ni0IeiNKxT57UzDqPtd25ACD"
path="/rest/api/2/project"

req=Request("https://"+ url+path)
auth_string=username+ ":"+ token
log.warning("auth string: "+ auth_string)
base=base64.b64encode(str.encode(auth_string))
log.warning("base64"+ base.decode())
base_str=base.decode("utf-8")
log.warning("base64 string: "+ base_str)
req.add_header("Authorization","Basic "+base_str)
req.add_header("Accept","application/json")
response=""
with urlopen(req) as resp_obj:
    response=resp_obj.read().decode("utf-8")
print(response)'''
class JiraHttp:
    def __init__(self):
        print("class initialised")
        self.response=""
    def set_host(self,host):
        self.host=host
    def get_host(self):
        return self.host
    def set_username(self,username):
        self.username=username
    def get_username(self):
        return self.username
    def set_token(self,token):
        self.token=token
    def get_token(self):
        return self.token
    def set_path(self,path):
        self.path=path
    def get_path(self):
        return self.path
    def get_response(self,url):
        req=Request(url)
        req.add_header("Authorization","Basic "+base64.b64encode(str.encode(self.username+ ":"+ self.token)).decode("utf-8"))
        req.add_header("Accept","application/json")
        r={"error":True}
        try:
            with urlopen(req) as resp_obj:
                r["response"]=resp_obj.read().decode("utf-8")
            r["error"]=False
        except HTTPError as error:
            r["response"]=str(error)
            log.warning(error)
        return json.dumps(r)
    def fetch_https_response(self):
        u="https://"+ self.host+self.path
        self.response=self.get_response(u)
        return self.response
    def fetch_http_response(self):
        u="http://"+ self.host+self.path
        self.response=self.get_response(u)
        return self.response
        
    
if __name__=="__main__":
    r=JiraHttp()
    r.set_host("aquacrmsoftware.atlassian.net")
    r.set_username("priyank@aquacrmsoftware.com")
    r.set_token("ni0IeiNKxT57UzDqPtd25ACDe")
    r.set_path("/rest/api/2/project")
    r.fetch_http_response()
    j_obj=json.loads(r.response)
    print(j_obj)
