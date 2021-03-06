from json import JSONDecodeError

import requests
import urllib3

from hesperidescli.configure import configure

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Client:
    def __init__(self):
        self.endpoint = configure.get_config('endpoint')
        auth = configure.get_config('auth')
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic %s' % auth,
            'Content-Type': 'application/json; charset=utf-8'
        }

    def get(self, path, params=None):
        return requests.get(self.endpoint + path, params=params, headers=self.headers,
                            verify=False)

    def delete(self, path, params=None):
        return requests.delete(self.endpoint + path, params=params, headers=self.headers,
                               verify=False)

    def post(self, path, params=None, body=None):
        if body:
            return requests.post(self.endpoint + path, params=params, data=body, headers=self.headers,
                                 verify=False)
        else:
            return requests.post(self.endpoint + path, params=params, headers=self.headers,
                                 verify=False, stream=True)

    def put(self, path, params=None, body=None):
        if body:
            return requests.put(self.endpoint + path, params=params, data=body, headers=self.headers,
                                verify=False)
        else:
            return requests.put(self.endpoint + path, params=params, headers=self.headers, verify=False)
