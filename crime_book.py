import pickle
import pandas as pd
import streamlit as st
import sqlite3


connection_obj = sqlite3.connect('E:/House-of-Hackers/Crime book/Crime_book.db')
#read the data from the database using pandas 
df = pd.read_sql_query("SELECT * FROM crime_book", connection_obj)


st.title("Crime Priority - Crime Book")

#write the df as a table in the streamlit
st.table(df.head())

#read the enws data
new_df = pd.read_csv("./crime-data/crime_priority.csv")
#read the model
model = pickle.load(open('./models/crime-priority.pkl','rb'))
#read the vectorizer
vectorizer = pickle.load(open('./models/crime-vectorizer.pkl','rb'))



def classify_text(text):
    # Convert the text into numerical features using the vectorizer
    X = vectorizer.transform(text)

    # Make a prediction using the trained classifier
    y_pred = model.predict(X)

    # Return the predicted category
    return y_pred


post = df['crime']
#convetr the post into a list
post = list(post)


# st.write(post)

# post = ["A woman reported being sexually harassed on public transport",
#          "A man was arrested for possessing illegal firearms.",
#          "Someone stole a laptop from a coffee shop.",
#          "A man was caught trespassing on private property.",
#          "A company discovered that one of its employees had embezzled funds."]
# st.write(post)

total_no_of_crimes = len(post)
st.subheader("Total number of crimes posted on crime book: {}".format(total_no_of_crimes))

area = df['area']
area = list(area)

name = df['name']
name = list(name)

time = df['timestamp']
time = list(time)


result = classify_text(post)
# print(result)
#extract the crime level from the new_df
levels = []
for i in range(len(result)):
    level = new_df[new_df['Crime'] == result[i]]
    levels.append(level.Level.values[0])

# out df
out_df = pd.DataFrame({'Time': time,'Crime': result, 'Description': post, 'Area': area, 'Name': name,'Priority': levels})
# print(out_df)
#sort the crime based on the level high to low
out_df = out_df.sort_values(by=['Priority'], ascending=False)

#now show out_df as a table in the streamlit
st.write("Top 3 crimes based on priority level")
st.table(out_df.head(3))