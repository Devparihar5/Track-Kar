# import mysql.connector
# from mysql.connector import Error

# # dbpassword = 'l;gdjokdfhgkjdfhgdfjkghdk'

# def data(val):
#     try:
#         # make connection with database
#         connection = mysql.connector.connect(host='localhost',
#                                              database='engineers',
#                                              user='root',
#                                              password='hskljghdskjghdkjghdfj')
#         # checking connections
#         if connection.is_connected():
#             cursor = connection.cursor()
#             query = "INSERT INTO suspect(name,number,number2,mail,alice,fname,mname,dob,gender,height,identy_mark,pre_address,perm_address,adhaar,pan,driving,other_docs,bank,crime,fir_no,st_name,theaft_no,img) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,load_file(%s));"
#             # query = "insert into peoples(name,number,mail,age,address,img) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#             # print(query)
#             cursor.execute(query, val)
#             connection.commit()
#             print(cursor.rowcount, "record inserted.")
#             # myresult = cursor.fetchall()
#             # print(myresult)
#         else:
#             pass

#     except Error as e:
#         numb = ("Error while connecting to MySQL", e)
#         print(numb)
#     finally:
#         # colse our server
#         if connection.is_connected():
#             cursor.close()
#             connection.close()


# xyz = 0

# while True:
#     name = input("Name:")
#     number = input("number1")
#     number2 = input("number2")
#     mail = input("mail:")
#     alice = input("Alice name:")
#     fname = input("Father Name:")
#     mname = input("Mother Name:")
#     dob = input("DOB:")
#     gender = input("Gender:")
#     height = input("Height:")
#     identy_mark = input("Identy Mark:")
#     pre_address = input("present address:")
#     perm_address = input("permanent address:")
#     adhaar = input("Adhar no:")
#     pan = input("pan no:")
#     driving = input("driving licence:")
#     other_docs = input("other docs:")
#     bank = input("bank:")
#     crime = input("What is the crime:")
#     fir_no = input("Fir No:")
#     st_name = input("Station Name:")
#     theaft_no = input("Theaft No:")
#     img = input("Image path")

#     val = (name, number, number2, mail, alice, fname, mname, dob, gender, height, identy_mark, pre_address,
#            perm_address, adhaar, pan, driving, other_docs, bank, crime, fir_no, st_name, theaft_no, img)
#     data(val)
#     if xyz == 1:
#         break
#     else:
#         xyz = xyz + 1







import sqlite3
  
# filename to form database
file = "Criminal_Database.db"
  
try:
  conn = sqlite3.connect(file)
  print("Database Sqlite3.db formed.")
except:
  print("Database Sqlite3.db not formed.")