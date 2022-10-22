#Stock Prediction Using Indicators
import pandas as pd #Pandas is used to analyze data.
import yfinance as yf #Used to get stock prices
import matplotlib as plt #For visulaization of graphs

#Data Collection And Sorting
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = tickers.Symbol.to_list()
tickers=[i.replace('.','-') for i in tickers]
tickers.pop(474)
tickers.pop(489)
#print(tickers)

#Defining The RSI Calculation
def RSI(asset):
    df = yf.download(asset,start='2022-01-01')
    return df