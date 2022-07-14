#Importing Libraries
import streamlit as st 
import pandas as pd 
import matplotlib as plt
import subprocess
import sys
import base64

st.title("Crypto currency web-app Data") #Title of the webpage

df = pd.read_csv("/home/shayan/Desktop/Code/Data Science/Cryptocurrency-data-web-app/Data.csv") #Importing our CSV
df = df.iloc[: , 1:] #Removing the first column

#Creating a button that refreshes the data by running the script
if st.button("Refresh Data") : 
    subprocess.run([f"{sys.executable}", "data.py"]) #Runs the script again to get the latest data
else : 
    pass

#Title of the sidebar
st.sidebar.header("Query the data")

#The user chooses the number of coins to display in the sidebar
num_coin = st.sidebar.slider('Number of coins to display', 1, 5000, 5000)
df = df[:num_coin]

st.dataframe(df)

# Download CSV data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df), unsafe_allow_html=True)