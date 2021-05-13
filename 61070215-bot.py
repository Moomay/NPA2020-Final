import requests
import time
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)



def getStatus():
    response = requests.get(
        url = 'https://10.0.15.116/restconf/data/ietf-interfaces:interfaces/interface=Loopback61070215',
        auth = ('admin', 'cisco'),
        headers = {
            'Accept': 'application/yang-data+json'
        },
        verify = False)
    lo61070215 = json.loads(response.content)

    return lo61070215['ietf-interfaces:interface']['enabled']
def sendMessage(mes, headersz):
    url = "https://webexapis.com/v1/messages"
    pay ='{"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3","text": "' + mes+ '"}'
    response = requests.request("POST", url, headers=headersz, data=pay)
def bot():
    headers = {
    'Authorization': 'Bearer ZGI0NjYzMmItYjlhYS00NzgwLTg5MjYtM2U4MTI2NGZmYzlkMmIwMzI2ZjgtMmZj_PF84_consumer',
    'Content-Type': 'application/json'
    }
    url_read = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3&max=1"
    oldMesId = 0
    while(1):
        isNewMessage = False
        response_mes = requests.request("GET", url_read, headers=headers)
        res = json.loads(response_mes.text)
        newMesId = res['items'][0]['id']
        newMes = res['items'][0]['text']
        if (newMesId != oldMesId):
            print("new message is "+ newMes)
            isNewMessage = True
        if (isNewMessage == True):
            if (newMes == "61070215"):
                if (getStatus()):
                    sendMessage("Loopback61070215 - Operational status is up", headers)
                else:
                    sendMessage("Loopback61070215 - Operational status is down", headers)

        oldMesId = newMesId
        time.sleep(1)

bot()