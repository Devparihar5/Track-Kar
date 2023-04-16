########################### db creattion ############################
# import sqlite3
  
# # filename to form database
# file = "Crime_book.db"
# try:
#   conn = sqlite3.connect(file)
#   print("Database Sqlite3.db formed.")
# except:
#   print("Database Sqlite3.db not formed.")


########################## db table creation ############################
import sqlite3

# try:
#     connection_obj = sqlite3.connect("./Crime_book.db")
#     print("Database connected.")
#     cursor_obj = connection_obj.cursor()
#     # drop table if exists
#     cursor_obj.execute("DROP TABLE IF EXISTS crime_book")

#     table = """CREATE TABLE crime_book (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(255) NOT NULL,
#         area VARCHAR(155) NOT NULL,
#         crime VARCHAR(500) NOT NULL,
#         timestamp VARCHAR(255) NOT NULL
#     );"""

#     cursor_obj.execute(table)
#     #enter data in table
#     print("Table is Ready")
# except:
#     print("Database not connected.")


# ########################## db table insertion ############################
# import sqlite3
import datetime
try:
    connection_obj = sqlite3.connect("./Crime_book.db")
    print("Database connected.")
    cursor_obj = connection_obj.cursor()
   
    #insert query 
    insert_query = """INSERT INTO crime_book (name, area, crime, timestamp) VALUES (?, ?, ?, ?)"""
    
    current_time = datetime.datetime.now()

    data_tuple = ("Raju", "Ranchi", "A man was arrested for selling drugs at a local market", current_time)
    cursor_obj.execute(insert_query, data_tuple)
    connection_obj.commit()
    print("Data inserted successfully.")
except:
    print("Database not connected.")