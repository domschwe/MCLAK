import csv
import mysql.connector

mydb = mysql.connector.connect(host='database-1.ccghvxtbfsoz.us-west-2.rds.amazonaws.com',
    user='admin',
    passwd='password',
    db='main_data')
cursor = mydb.cursor()

query = "select * from arrests";

cursor.execute(query)

for row in cursor:
  print(row)

#csv_data = csv.reader(file('students.csv'))
#for row in csv_data:

#   cursor.execute('INSERT INTO testcsv(names, \
#          classes, mark )' \
#          'VALUES("%s", "%s", "%s")', 
#          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
