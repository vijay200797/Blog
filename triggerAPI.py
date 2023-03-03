import requests
import json


URL = "http://localhost:8000/api/employeeClassBasedAPI/"
HEADERS ={'content-Type': 'application/json'}

def Post():
    data = {'FirstName' : 'Sumit',
            'LastName' : 'Kumar ',
            'EmailID' : 'sumit@abc.com',
            'EmployeeCode' : 'EC0006',
            'Active': "1"
            }
    data = json.dumps(data)
    response = requests.post(url=URL, data= data, headers=HEADERS)
    rvalue = response.json()
    print(rvalue)

def Put():
    data = {
            'id': 13,
            'FirstName' : 'John',
            'LastName' : 'Dick',
            'EmailID' : 'John@abc.com',
            'EmployeeCode' : 'EC0007',
            'Active': "1"
            }
    data = json.dumps(data)
    response = requests.put(url=URL, data= data, headers=HEADERS)
    rvalue = response.json()
    print(rvalue)


def Get(id=None):
    data = {'id': id}
    data = json.dumps(data)
    response = requests.get(url=URL, data= data, headers=HEADERS)
    rvalue = response.json()
    print(rvalue['data'])
    print(rvalue['status'])

def Delete():
    data = {'id': 8}
    data = json.dumps(data)
    response = requests.delete(url=URL, data= data, headers=HEADERS)
    rvalue = response.json()
    print(rvalue['message'])
    print(rvalue['status'])

# Post() 
Get(13)
Put()
Get(13)