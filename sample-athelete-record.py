import sys
sys.path.append("c:\\users\\panne\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\\localcache\\local-packages\\python38\\site-packages")
import psycopg2
import requests
import json

#runverve URL & token details
myToken = '8fd5cd77d9f83af060344d907e34cc9b2e3b0dc5'
myUrl = 'https://www.strava.com/api/v3/athlete'
head = {'Authorization': 'Bearer {}'.format(myToken)}

#logged in athlete details in JSON
response = requests.get(myUrl, headers=head)
athlete_details = json.loads(response.text)
print(response.status_code)
print(athlete_details)

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='admin', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Insert the JSON value into the table
insert_query = "INSERT INTO ATHLETE_STRAVA (ID,FIRST_NAME,LAST_NAME,SEX,CITY,STATE,COUNTRY,PROFILE ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(insert_query, (athlete_details['id'],athlete_details['firstname'],athlete_details['lastname'],athlete_details['sex'],athlete_details['city'],athlete_details['state'],athlete_details['country'],athlete_details['profile']))
#result = cursor.fetchone()[0]

print("Record got inserted")
