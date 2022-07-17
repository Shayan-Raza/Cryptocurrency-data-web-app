#Importing Libraries
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
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
st.dataframe(df_coins) #Showing the dataframe with the selected coins

# Download CSV data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_coins), unsafe_allow_html=True)

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

st.write(f"## Plot {percent_timeframe} for {selected_coin}") #Title of the plot

#Filtering and creating plots
#Using try and except and when user doesnt select coin theres an error
try : 
    if percent_timeframe == "90d" : 
        df_change["quote_USD_percent_change_90d"].plot(kind="barh")
        st.pyplot(plt)
    elif percent_timeframe == "60d" : 
        df_change["quote_USD_percent_change_60d"].plot(kind="barh")
        st.pyplot(plt)
    elif percent_timeframe == "30d" : 
        df_change["quote_USD_percent_change_30d"].plot(kind="barh")
        st.pyplot(plt)
    elif percent_timeframe == "7d" : 
        df_change["quote_USD_percent_change_7d"].plot(kind="barh")
        st.pyplot(plt)
    elif percent_timeframe == "24h" : 
        df_change["quote_USD_percent_change_24h"].plot(kind="barh")
        st.pyplot(plt)
    elif percent_timeframe == "1h" : 
        df_change["quote_USD_percent_change_1h"].plot(kind="barh")
        st.pyplot(plt)
except: 
    pass

# Price displayer
st.write("## Prices")

df_price = pd.concat([df_coins.symbol, #Df with symbol of the coin and its price
    df_coins.quote_USD_price,
], axis=1,)

#Sort df by index
df_price = df_price.sort_index(axis=0)
print(df_price)

#Preparing variable for displaying
price = df_price["quote_USD_price"]
price = price.to_string(index=False)
price = price.split()

selected_coin = df_price.symbol
#Displaying the price

counter = 0 #Counter will be used later for indexing

#Using for loop to display price of every coin selected
for coin in selected_coin : 
    st.write(f"The price for {coin} is {price[counter]}")
    counter = counter + 1 
