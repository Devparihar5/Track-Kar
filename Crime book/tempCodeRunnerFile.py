########## db table insertion ############################
# import sqlite3

# try:
#     connection_obj = sqlite3.connect("./Crime_book.db")
#     print("Database connected.")
#     cursor_obj = connection_obj.cursor()
   
#     #insert query 
#     insert_query = """INSERT INTO crime_book (name, area, crime, timestamp) VALUES (?, ?, ?, ?)"""

#     data_tuple = ("Raju", "Ranchi", "