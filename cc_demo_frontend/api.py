import requests

url = "http://127.0.0.1:8000/register/"

payload="{\n    \"api_key\":\"adawxsaxaawdw\",\n    \"secret_key\":\"dawedxxxsawadwae\",\n    \"user\":{\n        \"password\":\"11323\",\n        \"email\":\"dwadwea12@acdascdas.com\",\n        \"first_name\":\"cascasdcas\",\n        \"last_name\":\"xaxasdac\"\n    }\n\n\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=gQYTzMYqDtmPyKGZByVHSjb3lUcQvziWtrnDE9kIgZCIPpn2AYYzb7eLJtXK6o6k; sessionid=qn3kqnjzfbp78ujawujdyb9j4m27t1zs'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)