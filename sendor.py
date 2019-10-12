#import requests library for making REST calls
import requests
import json
import six

#specify url
url = 'http://localhost:5000/todo/api/v1.0/tasks/2'

token = "my token"

data = {
        "task": "Chicekn",
        "description": "myAgentName",
        "done": False,
        "title": ""
        }


headers = {"Content-Type": "application/json"}

#Call REST API
response = requests.put(url, data=json.dumps(data), headers=headers)

#Print Response
print(response.text)



#specify url
url = 'http://localhost:5000/todo/api/v1.0/tasks'

token = "my token"

data = {
        "task": "Chicekn",
        "description": "myAgentName",
        "done": False,
        "title": ""
        }


headers = {"Content-Type": "application/json"}

#Call REST API
response = requests.post(url, data=json.dumps(data), headers=headers)

#Print Response
print(response.text)
