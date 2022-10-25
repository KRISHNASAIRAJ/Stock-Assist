import streamlit as st
import pandas as pd#Analysis of data
import yfinance as yf
st.set_page_config(page_title='Stock Assist',page_icon='📈')
st.title('Stock Assist')
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = tickers.Symbol.to_list()
tickers=[i.replace('.','-') for i in tickers]
tickers.pop(474)
tickers.pop(489)
dropdown=st.multiselect('Pick your asset',tickers)
startd = st.date_input('Start', value = pd.to_datetime('2022-10-01'))
end = st.date_input('End', value = pd.to_datetime('today'))
def RSI(asset):
    dataframe = yf.download(asset,start=startd)
    #dataframe['MA200']=dataframe['Adj Close'].rolling(window=200).mean()
    dataframe['Price Change']=dataframe['Adj Close'].pct_change()
    dataframe['Upmove']=dataframe['Price Change'].apply(lambda x: x if x>0 else 0)
    dataframe['Downmove']=dataframe['Price Change'].apply(lambda x: abs(x) if x<0 else 0)
    dataframe['AvgUp']=dataframe['Upmove'].ewm(span=19).mean()
    dataframe['AvgDown']=dataframe['Downmove'].ewm(span=19).mean()
    dataframe=dataframe.dropna()
    dataframe['RS']=dataframe['AvgUp']/dataframe['AvgDown']
    dataframe['RSI']=dataframe['RS'].apply(lambda x:100-(100/(1+x)))
    #dataframe.loc[dataframe['']&(dataframe['RSI']<30),'Buy']='Yes'
    return dataframe
st.table(RSI(dropdown))
