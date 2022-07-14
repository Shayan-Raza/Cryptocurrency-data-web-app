#Importing Libraries
import streamlit as st 
import pandas as pd 
import matplotlib as plt
import subprocess
import sys

#Creating a button if clicked refreshes the data

st.title("Crypto currency web-app Data") #Title of the webpage

df = pd.read_csv("/home/shayan/Desktop/Code/Data Science/Cryptocurrency-data-web-app/Data.csv") #Importing our CSV

if st.button("Refresh Data") : 
    subprocess.run([f"{sys.executable}", "data.py"]) #Runs the script again to get the latest data
else : 
    pass
