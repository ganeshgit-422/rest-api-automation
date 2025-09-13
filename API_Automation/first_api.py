import requests
import json

get_resp = requests.get(url="https://reqres.in/api/users?page=2")
data = get_resp.json()
json_resp = json.dumps(data, indent= 4
                       )
# print(get_resp.json())
print(json_resp)