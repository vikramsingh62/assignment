import requests

resp = requests.get("https://reqres.in/api/users?page=2")
print (resp)
res_code = resp.status_code
assert res_code == 201 , "Code doesnot match"
resp.text