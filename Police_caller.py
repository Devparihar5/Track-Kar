from truecallerpy import search_phonenumber, bulk_search
import streamlit as st
import sys
import requests

# id = "a1i0R--cvttz2FZ-ky8i5vx2XFHWFlKr-cHOnPQyF153JBj7l9iRL2_Ej6dt93dP"
id = "a1i0M--ea2dl4F_VFzsb8c4kJPHQhgawDHdKtchAGFPWCsWCKCUm3my1z6kWl2lY"
num = '9059623015'
# df=bulk_search('9059623015, 8963002842',"IN", id)
df = search_phonenumber(num, "IN", id)
#
st.subheader("Mobile Number Profile: "+ str(num))
st.write(df)

try:
        name = df['data'][0]['name']
except:
        name = ' '
try:
        mail = df['data'][0]['internetAddresses'][0]['id']
except:
        mail = ' '
try:
        address = df['data'][0]['addresses'][0]['city'] + ", " + df['data'][0][
        'addresses'][0]['address']
except:
        address = ' '
# print(add)
try:
        link = df['data'][0]['image']
except:
        link = 'https://icon-library.com/images/unknown-person-icon/unknown-person-icon-10.jpg'
try:
        age = df['data'][0]['birthday']
except:
        age = ' '


#download the image from the link
r = requests.get(link, allow_redirects=True)
open('image.jpg', 'wb').write(r.content)
st.image('./image.jpg', width=100, caption='Profile Picture', use_column_width=True)
st.subheader("Name: "+ str(name))
st.subheader("Email: "+ str(mail))
st.subheader("Address: "+ str(address))
st.subheader("Age: "+ str(age))
