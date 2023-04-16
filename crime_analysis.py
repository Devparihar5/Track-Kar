import streamlit as st
import pandas as pd

df = pd.read_csv('./crime-data/train.csv.zip')
# print(df.head())

# write a header usiong streamlit of crime analysis
st.title('Crime Data Analysis')
st.subheader('Sample Reports data')
#show some sample dataset on the screen
st.write(df.head())

#show the image on screen
st.subheader('-------------------------------------------------------------------------------')
st.image('./images/incidents.png')
st.subheader('-------------------------------------------------------------------------------')
st.image('./images/weekday.png')
st.subheader('-------------------------------------------------------------------------------')
st.image('./images/crime_category.png')
st.subheader('-------------------------------------------------------------------------------')
st.subheader('Incidents per day for every district')
st.image('./images/cities.png')
st.subheader('-------------------------------------------------------------------------------')
st.image('./images/geographic.png')