from flask import Flask, render_template, request
import pandas as pd
import random
import sqlite3
import os
import datetime

#list of random areas like ranchi, patna, delhi, mumbai, etc
areas = ["Ranchi","Delhi","Patna","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad","Pune","Jaipur","Lucknow","Kanpur","Nagpur","Indore","Thane","Bhopal","Pimpri-Chinchwad","Patna","Vadodara","Ghaziabad","Ludhiana","Agra","Nashik","Faridabad","Meerut","Rajkot","Kalyan-Dombivali","Vasai-Virar","Varanasi","Srinagar","Aurangabad","Dhanbad","Amritsar","Navi Mumbai","Allahabad","Ranchi","Howrah","Coimbatore","Jabalpur","Gwalior","Vijayawada","Jodhpur","Madurai","Raipur","Kota","Guwahati","Chandigarh","Solapur","Hubli-Dharwad","Bareilly","Moradabad","Mysore","Aligarh","Gurgaon","Jalandhar","Tiruchirappalli","Bhubaneswar","Salem","Warangal","Mira-Bhayandar","Thiruvananthapuram","Bhiwandi","Saharanpur","Guntur","Bikaner","Amravati","Noida","Jamshedpur","Bhilai Nagar","Cuttack","Firozabad","Kochi","Nellore","Bhavnagar","Dehradun","Durgapur","Asansol","Rourkela","Nanded","Kolhapur","Ajmer","Akola","Gulbarga","Jamnagar","Ujjain","Loni","Siliguri","Jhansi","Ulhasnagar","Jammu","Sangli-Miraj & Kupwad","Mangalore","Erode","Belgaum","Malegaon","Jalgaon","Udaipur","Maheshtala","Kozhikode","Kurnool","Bokaro Steel City","Rajahmundry","Davanagere","Dhule","Korba","Bhilwara","Bhagalpur","Muzaffarnagar","Ahmednagar","Kollam","Akbarpur","Bilaspur","Shahjahanpur","Brahmapur"]

#list of random names like raju papu, etc
names = ["Raju","Papu","Rahul","Rohit","Raj","Rajesh","Rajat","Rajeev","Rajiv","Rajkumar","Rajnish","Rajpal","Rajveer","Rajvir","Rakesh","Rakshit","Ram","Raman","Ramandeep","Ramani","Ramandeep","Ramandeep"]




app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/notification')
def notification():
    return render_template('notification.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')



@app.route('/post', methods=['POST'])
def handle_post():
    post_content = request.form['post_content']
    # get the curretn time stamp in seconds
    current_time = datetime.datetime.now()
    # get a random area from the list
    area = random.choice(areas)
    # get a random name from the list
    name = random.choice(names)

    try:
        connection_obj = sqlite3.connect("./Crime_book.db")
        print("Database connected.")
        cursor_obj = connection_obj.cursor()
    
        #insert query 
        insert_query = """INSERT INTO crime_book (name, area, crime, timestamp) VALUES (?, ?, ?, ?)"""
        
        data_tuple =  (name, area, post_content, current_time)
        cursor_obj.execute(insert_query, data_tuple)
        connection_obj.commit()
        print("Data inserted successfully.")
    except:
        print("Database not connected.")
    finally:
        connection_obj.close()
        print("Database connection closed.")
    
    print("Post saved in databaase.")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port="9024")