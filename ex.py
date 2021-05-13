import requests
import time
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

response = requests.get(
    url = 'https://10.0.15.116/restconf/data/ietf-interfaces:interfaces/interface=Loopback61070215',
    auth = ('admin', 'cisco'),
    headers = {
        'Accept': 'application/yang-data+json'
    },
    verify = False)
lo61070215 = json.loads(response.content)

print(type(lo61070215['ietf-interfaces:interface']['enabled']))