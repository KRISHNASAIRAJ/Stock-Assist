# Stock Prediction Using Indicators
import pandas as pd  # Pandas is used to analyze data.
import yfinance as yf  # Used to get stock prices
import matplotlib as plt  # For visulaization of graphs
import streamlit as st  # To Deploy as web app
# Page Properties
st.set_page_config(page_title='Stock Assist', page_icon='📈')
st.title('Stock Assist')
# Data Collection And Sorting
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = tickers.Symbol.to_list()
tickers = [i.replace('.', '-') for i in tickers]
tickers.pop(474)
tickers.pop(489)
# Making Buttons
dropdown = st.multiselect('Pick your asset', tickers)
startd = st.date_input('Start', value=pd.to_datetime('2022-10-01'))
end = st.date_input('End', value=pd.to_datetime('today'))
# RSI Algo
def RSI(asset):
    df = yf.download(asset, start=startd)
    return df
st.table(RSI(dropdown))