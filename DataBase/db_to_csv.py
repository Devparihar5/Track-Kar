#extract Details from Database
import sqlite3
import cv2
import pandas as pd
conn = sqlite3.connect('E:/my app -original/Criminal_Database.db')
print("Opened database successfully")

# extract the table from the database and save that table into a csv file

df = pd.read_sql_query("SELECT * from suspect", conn)
print(df.head(0))
