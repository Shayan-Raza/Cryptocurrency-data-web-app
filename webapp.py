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
df.columns = ['id', 'name', 'symbol', 'slug', 'num_market_pairs', 'date_added', #Renaming columns for efficiency
       'tags', 'max_supply', 'circulating_supply', 'total_supply', 'platform',
       'cmc_rank', 'self_reported_circulating_supply',
       'self_reported_market_cap', 'tvl_ratio', 'last_updated',
       'quote_USD_price', 'quote_USD_volume_24h',
       'quote_USD_volume_change_24h', 'quote_USD_percent_change_1h',
       'quote_USD_percent_change_24h', 'quote_USD_percent_change_7d',
       'quote_USD_percent_change_30d', 'quote_USD_percent_change_60d',
       'quote_USD_percent_change_90d', 'quote_USD_market_cap',
       'quote_USD_market_cap_dominance', 'quote_USD_fully_diluted_market_cap',
       'quote_USD_tvl', 'quote_USD_last_updated', 'platform_id',
       'platform_name', 'platform_symbol', 'platform_slug',
       'platform_token_address']

#Creating a button that refreshes the data by running the script
if st.button("Refresh Data") : 
    subprocess.run([f"{sys.executable}", "data.py"]) #Runs the script again to get the latest data
else : 
    pass

#Title of the sidebar
st.sidebar.header("Query the data")

#Lets the user select their coin
selected_coin = st.sidebar.multiselect("Choose your coin (Symbol)", df["symbol"])
df_coins = df[ (df["symbol"].isin(selected_coin)) ] # Filtering data

#The user chooses the percentage change time frame
percent_timeframe = st.sidebar.selectbox("Percent change time frame",
                                    ["90d","60d","30d","7d","24h","1h"])

#Preparing data for filtering according to percentage change
df_change = pd.concat([df_coins.symbol, #Creating a new df with symbol and change columns 
    df_coins.quote_USD_percent_change_90d, 
    df_coins.quote_USD_percent_change_60d, 
    df_coins.quote_USD_percent_change_30d, 
    df_coins.quote_USD_percent_change_7d, 
    df_coins.quote_USD_percent_change_24h,
    df_coins.quote_USD_percent_change_1h,
], axis=1)

st.dataframe(df_coins) #Showing the dataframe with the selected coins

# Download CSV data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_coins), unsafe_allow_html=True)