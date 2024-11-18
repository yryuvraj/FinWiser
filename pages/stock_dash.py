import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas_ta as ta
from stocknews import StockNews

st.title("FinWiser: Advanced Financial Dashboard")


default_ticker = "F"
ticker = st.sidebar.text_input("Enter Ticker", default_ticker)
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")


data = yf.download(ticker, start=start_date, end=end_date)

fig = px.line(
    data, x=data.index, y=data["Adj Close"], title=f"{ticker} - Adjusted Close Price"
)
st.plotly_chart(fig)

x = go.Figure(
    data=[
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
        )
    ]
)
st.header("Candlestick Chart")
x.update_layout(title=f"{ticker} - Candlestick Chart")
st.plotly_chart(x)


pricing_data, news, tech_indicator, advanced_analysis = st.tabs(
    ["Pricing Data", "News", "Technical Indicators", "Advanced Analysis"]
)

with pricing_data:
    st.header("Price Movements and Returns")
    st.write("Detailed price movements and metrics:")
    data["%Change"] = data["Adj Close"] / data["Adj Close"].shift(1) - 1
    st.write(data)

    annual_return = data["%Change"].mean() * 252 * 100
    st.write(f"Annual Return: {annual_return:.2f}%")

    stddev = np.std(data["%Change"]) * np.sqrt(252) * 100
    st.write(f"Volatility (Standard Deviation): {stddev:.2f}%")

    sharpe_ratio = annual_return / stddev
    st.write(f"Risk-Adjusted Return (Sharpe Ratio): {sharpe_ratio:.2f}")

with news:
    st.header(f"News for {ticker}")
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):  
        st.subheader(f"News {i + 1}")
        st.write(df_news["published"][i])
        st.write(df_news["title"][i])
        st.write(df_news["summary"][i])
        st.write(f"Title Sentiment: {df_news['sentiment_title'][i]}")
        st.write(f"News Sentiment: {df_news['sentiment_summary'][i]}")

with tech_indicator:
    st.header("Technical Indicators")
    st.write("Select and calculate popular indicators.")

    
    st.subheader("Relative Strength Index (RSI)")
    rsi_period = st.slider("RSI Period", 7, 50, 14)
    data["RSI"] = ta.rsi(data["Close"], length=rsi_period)
    st.line_chart(data[["RSI"]])

    
    st.subheader("MACD")
    macd = ta.macd(data["Close"])
    data = pd.concat([data, macd], axis=1)
    st.line_chart(data[["MACD_12_26_9", "MACDs_12_26_9", "MACDh_12_26_9"]])

    
    st.subheader("Bollinger Bands")
    bbands = ta.bbands(data["Close"], length=20, std=2.0)  
    if bbands is not None:
        data = pd.concat([data, bbands], axis=1)
        bb_lower = bbands.columns[0]  
        bb_middle = bbands.columns[1]
        bb_upper = bbands.columns[2]
        st.line_chart(data[[bb_lower, bb_middle, bb_upper, "Close"]])
    else:
        st.warning("Bollinger Bands calculation failed. Ensure sufficient data is available.")

with advanced_analysis:
    st.header("Advanced Analysis")
    
    
    st.subheader("Moving Averages")
    ma_short = st.slider("Short-Term Moving Average Period", 5, 50, 20)
    ma_long = st.slider("Long-Term Moving Average Period", 50, 200, 100)
    data["Short_MA"] = data["Close"].rolling(window=ma_short).mean()
    data["Long_MA"] = data["Close"].rolling(window=ma_long).mean()
    ma_chart = px.line(data, x=data.index, y=["Short_MA", "Long_MA", "Close"], title="Moving Averages")
    st.plotly_chart(ma_chart)

    
    st.subheader("Pattern Detection")
    st.write("Detect head-and-shoulders or other patterns (future implementation).")
    
    
    st.subheader("Statistical Insights")
    st.write("Descriptive statistics for the selected stock:")
    st.write(data.describe())

    
    st.subheader("Custom Indicator")
    st.write("Build your own analysis metrics using column names like 'Open', 'Close', 'High', 'Low', and 'Volume'.")
    
    
    st.write("Available columns: ", list(data.columns))
    
    custom_formula = st.text_input("Enter custom formula (e.g., (Close - Open) / Volume):")
    try:
        
        data["Custom_Indicator"] = data.eval(custom_formula)
        st.line_chart(data["Custom_Indicator"])
    except Exception as e:
        st.error(f"Error in formula: {e}")
