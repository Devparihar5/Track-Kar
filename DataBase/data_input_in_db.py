# #write details in database
# # Importing Sqlite3 Module
# import sqlite3

# def convertToBinaryData(filename):
#     # Convert binary format to images 
#     # or files data
#     with open(filename, 'rb') as file:
#         blobData = file.read()
#     return blobData

# try:
#     connection_obj = sqlite3.connect('E:/my app -original/Criminal_Database.db')
#     print("Connected to SQLite")

#     cursor_obj = connection_obj.cursor()
    
#     #enter data in table
#     print("Table is Ready")
#     query = """INSERT INTO suspect (name, number, mail, address, dob, picture) 
#     VALUES ('Dev','7854218956','raju@gmail.com','Bhopal','12/12/1998');"""
#     cursor_obj.execute("INSERT INTO suspect (name, number, mail, address, dob, picture) VALUES (?,?,?,?,?,?)", (name, number, mail, address, dob, picture))
#     connection_obj.commit()
#     print("Data is inserted successfully")
#     print("Operation done successfully")
#     connection_obj.close()
#     print("the sqlite connection is closed")


import sqlite3


# Function for Convert Binary Data
# to Human Readable Format
def convertToBinaryData(filename):
	# Convert binary format to images
	# or files data
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData


def insertBLOB(fir_no,name,number,mail,address,dob,picture):
	try:
		# Using connect method for establishing
		# a connection
		sqliteConnection = sqlite3.connect('E:/House-of-Hackers/Criminal_Database.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")
		
		# insert query
		sqlite_insert_blob_query = """ INSERT INTO suspect
								(fir_no,name, number, mail, address, dob, picture) VALUES (?,?,?,?,?,?,?)"""
		
		empPhoto = convertToBinaryData(picture)
		
		# Convert data into tuple format
		data_tuple = (fir_no,name,number,mail,address,dob, empPhoto)
		# print(data_tuple)
		# using cursor object executing our query
		cursor.execute(sqlite_insert_blob_query, data_tuple)
		sqliteConnection.commit()
		print("Image and file inserted successfully as a BLOB into a table")
		cursor.close()

	except sqlite3.Error as error:
		print("Failed to insert blob data into sqlite table", error)
	
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("the sqlite connection is closed")



# insertBLOB(1534,"Dev","7854218956","dev@gmail.com","Jodhpur, Rajasthan","02/07/2001","E:/my app -original/static/sus_img/1.jpg")
insertBLOB(1989,"Gopika Varsini","7854218955","Gopika@gmail.com","Andhra Pradesh","06/04/2002","E:/House-of-Hackers/static/imgs/gopika.jpg")
print("Image and file inserted successfully as a BLOB into a table")