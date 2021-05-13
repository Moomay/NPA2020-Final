import requests
import time
import json

url_read = "https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYjExY2ZlYTAtYjMzOC0xMWViLWI2YzktZDNmZWJmNjZkYTFi&max=1"
url = "https://webexapis.com/v1/messages"


#payload="""{
#  "roomID": "Y2lzY29zcGFyazovL3VzL1JPT00vYjExY2ZlYTAtYjMzOC0xMWViLWI2YzktZDNmZWJmNjZkYTFi",
#  "text": "Best is the Best"
#}"""

headers = {
  'Authorization': 'Bearer ZGI0NjYzMmItYjlhYS00NzgwLTg5MjYtM2U4MTI2NGZmYzlkMmIwMzI2ZjgtMmZj_PF84_consumer',
  'Content-Type': 'application/json'
}

old_mes = 0
while(1):
    isNew = False
    response_mes = requests.request("GET", url_read, headers=headers)
    res = json.loads(response_mes.text)
    new_mes = res['items'][0]['id']
    if (new_mes != old_mes):
        print("new_message is "+ res['items'][0]['text'])
        isNew = True
    if (isNew == True):
        if (res['items'][0]['text'] == "61070215"):
            pay ="""{
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYjExY2ZlYTAtYjMzOC0xMWViLWI2YzktZDNmZWJmNjZkYTFi",
  "text": "GO!"
}"""
            response = requests.request("POST", url, headers=headers, data=pay)
    old_mes = new_mes
    time.sleep(1)


#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
