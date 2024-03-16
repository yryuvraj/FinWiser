import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

st.title("FinWiser")
default_ticker = "F"
ticker = st.sidebar.text_input("Enter Ticker", default_ticker)
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

data = yf.download(ticker, start=start_date, end=end_date)

fig = px.line(data, x=data.index, y=data['Adj Close'], title="Time Series with Rangeslider")
st.plotly_chart(fig)

x = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])

st.header("Candle Stick Chart")
x.update_layout(title="Candlestick Chart")
st.plotly_chart(x)

pricing_data, fundatmental_data, news, tech_indicator= st.tabs(["Pricing Data", "Fundamental Data", "News", "Technical Indicators"])

with pricing_data:
    st.header("Price Movements")
    st.write("Highs and Lows, with proper rich data from Yahoo Finance API")
    data2 = data
    data2['%Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    st.write(data2)
    
    annual_return = data2['%Change'].mean() * 252 * 100 
    # ignoring holidays-kyuki investor ko pagal banana hai (logic behind 252)
    st.write(f"Annual Return: ", annual_return, "%")
    
    stddev = np.std(data2['%Change'])*np.sqrt(252)*100
    st.write("Volatility or Standard Deviation is:", stddev, "%")
    st.write("Risk Adjusted Return: Sharpe Ratio : ", annual_return/stddev, "%")

from alpha_vantage.fundamentaldata import FundamentalData  
with fundatmental_data:
    st.header("Fundamental Data")
    key = 'LAIZ601ZA7O2FULW'
    fd = FundamentalData(key, output_format='pandas')
    st.subheader("Balance Sheet")
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader("Income Statement")
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader("Cash Flow Statement")
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)
    
from stocknews import StockNews
with news:
    st.header(f'News of {ticker}')
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment: {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment: {news_sentiment}')

import pandas_ta as ta   
with tech_indicator:
    st.header("Technical Indicators")
    df = pd.DataFrame()
    ind_list = df.ta.indicators(as_list=True)
    technical_indicator = st.selectbox("Select Indicator", options=ind_list)
    method = technical_indicator
    indicator = pd.DataFrame(getattr(ta, method)(low=data['Low'], close=data['Close'], high=data['High'], open=data['Open'], volume=data['Volume']))
    indicator['Close'] = data['Close']
    xyz = px.line(indicator)
    st.plotly_chart(xyz)
    st.write(indicator)
    