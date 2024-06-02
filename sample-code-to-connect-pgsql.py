import sys
sys.path.append("c:\\users\\panne\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0\\localcache\\local-packages\\python38\\site-packages")
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='admin', host='127.0.0.1', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Create Employee Table
cursor.execute('''CREATE TABLE ATHLETE_STRAVA (
   ID INT,
   FIRST_NAME VARCHAR(255),
   LAST_NAME VARCHAR(255),
   SEX VARCHAR(255),
   CITY VARCHAR(255),
   STATE VARCHAR(255),
   COUNTRY VARCHAR(255),
   PROFILE VARCHAR(255)  
);''')

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()