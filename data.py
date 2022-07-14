# Importing libraries
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import requests
import json
import pandas as pd

import api_key #Importing the file with my api key

API = api_key.api #Creating a variable with my api key

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
  "start":"1",
  "limit":"5000",
  "convert":"USD"
}
headers = {
  "Accepts": "application/json",
  "X-CMC_PRO_API_KEY": API,
}

resp = requests.get(url, params=parameters, headers=headers)
jsondata = json.loads(resp.text)
CoinDF = pd.json_normalize(jsondata['data']) #Converting json data to pandas dataframe

CoinDF.to_csv("Data.csv") #Exporting to csv