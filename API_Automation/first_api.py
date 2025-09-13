import requests
import json

insert_record = {
    "name": "ganesh",
    "job": "IT"
}
headers = {"content-type":"application/json","x-api-key": "reqres-free-v1"}
post_resp = requests.post(url="https://reqres.in/api/users" , json=insert_record, headers = headers)
print(post_resp.status_code)
print(json.dumps(post_resp.json()))