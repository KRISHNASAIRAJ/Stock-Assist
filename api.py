import streamlit as st
import pandas as pd
import yfinance as yf
st.set_page_config(page_title='Stock Assist',page_icon='📈')
st.title('Stock Assist')
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = tickers.Symbol.to_list()
tickers=[i.replace('.','-') for i in tickers]
tickers.pop(474)
tickers.pop(489)
dropdown=st.multiselect('Pick your asset',tickers)
start = st.date_input('Start', value = pd.to_datetime('2022-10-01'))
end = st.date_input('End', value = pd.to_datetime('today'))