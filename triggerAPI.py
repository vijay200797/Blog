import json
import requests



URL = "http://localhost:8000/post/employeeAPI/"
HEADER = {'content-Type': 'application/json'}
def GetEmployee():
    obj = requests.get(url=URL, headers=HEADER)
    rvalue = obj.json()
    print(rvalue)

def PostEmployee():
    data = {
        'Name': 'Ram Avtar',
        'EmpCode': 'EC02',
        'EmpAddress': "1"
    }

    json_data = json.dumps(data)
    obj = requests.post(url=URL, headers=HEADER, data=json_data)
    rvalue = obj.json()
    print(rvalue)


# GetEmployee()
PostEmployee()