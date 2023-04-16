#extract Details from Database
import sqlite3
conn = sqlite3.connect('E:/my app -original/Criminal_Database.db')
print("Opened database successfully")

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

# cursor = conn.execute("SELECT criminal_id, name, number, mail, address, dob, picture from suspect")
cursor = conn.execute("Select * from suspect where fir_no = 1124")
myresult = cursor.fetchall()
print(myresult)
# cursor = myresult[0]
# print(cursor[2])
# print(cursor)

    
    
print("Operation done successfully")
conn.close()



