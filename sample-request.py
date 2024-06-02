import sys
sys.path.append("c:\\users\\panne\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\\localcache\\local-packages\\python38\\site-packages")
import requests
import json

myToken = '8fd5cd77d9f83af060344d907e34cc9b2e3b0dc5'
myUrl = 'https://www.strava.com/api/v3/athlete'
head = {'Authorization': 'Bearer {}'.format(myToken)}

response = requests.get(myUrl, headers=head)
print(response.status_code)

my_json = json.loads(response.text)
print(my_json)