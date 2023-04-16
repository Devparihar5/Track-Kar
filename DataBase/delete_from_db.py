#delete Details from Database
import sqlite3
conn = sqlite3.connect('E:/my app -original/Criminal_Database.db')
print("Opened database successfully")


# delete the the row where the fir_no is 1124
conn.execute("DELETE from suspect where fir_no = 1124")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

