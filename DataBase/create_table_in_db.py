
# Importing Sqlite3 Module
import sqlite3
import cv2
try:
    connection_obj = sqlite3.connect('E:/my app -original/Criminal_Database.db')
    print("Connected to SQLite")

    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute("DROP TABLE IF EXISTS suspect")
    
    table = """ CREATE TABLE suspect (
                criminal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                fir_no INTEGER NOT NULL,
                name CHAR(150),
                number CHAR(150),
                mail CHAR(150),
                address CHAR(150),
                dob CHAR(150),
                picture BLOB NOT NULL
            ); """
    

    cursor_obj.execute(table)
    #enter data in table
    print("Table is Ready")
 
except sqlite3.Error as error:
    print("Failed to connect with sqlite3 database", error)
finally:
    if connection_obj:
        connection_obj.close()
        print("the sqlite connection is closed")






