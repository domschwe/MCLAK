import pandas as pd
import mysql.connector


#this establishes a connection to the AWS RDS
mydb = mysql.connector.connect(host='database-1.ccghvxtbfsoz.us-west-2.rds.amazonaws.com',
    user='admin',
    passwd='password',
    db='main_data')
cursor = mydb.cursor()

#this pulls in the data from the API 
data = pd.read_csv('https://data.cityofnewyork.us/resource/8h9b-rp9u.csv')


#defining the insert command
query = 'INSERT INTO Persons (LastName , FirstName) VALUES (%s,%s)'
number = 0;
number += 1

for index, row in data.iterrows():
  cursor.execute(query,('fekadu','sami'))



mydb.commit()
cursor.close()
print "Run Completed"
