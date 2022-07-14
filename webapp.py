#Importing Libraries
import streamlit as st 
import pandas as pd 
import matplotlib as plt
import subprocess
import sys

st.title("Crypto currency web-app Data") #Title of the webpage

df = pd.read_csv("/home/shayan/Desktop/Code/Data Science/Cryptocurrency-data-web-app/Data.csv") #Importing our CSV

#Creating a button that refreshes the data by running the script
if st.button("Refresh Data") : 
    subprocess.run([f"{sys.executable}", "data.py"]) #Runs the script again to get the latest data
else : 
    pass
