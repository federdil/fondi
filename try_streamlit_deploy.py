import streamlit as st
import yfinance as yf
import pandas as pd

# App Title
st.title("Stock Dashboard with Yahoo Finance")

# Sidebar for User Inputs
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL", help="Enter the stock ticker symbol (e.g., AAPL, MSFT)")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Fetch Stock Data
if ticker:
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        if not stock_data.empty:
            # Display Stock Information
            st.subheader(f"Stock Data for {ticker.upper()} from {start_date} to {end_date}")
            st.dataframe(stock_data)

            # Line Chart of Closing Prices
            st.subheader(f"Closing Price Trend for {ticker.upper()}")
            st.line_chart(stock_data['Close'])

            # Moving Average
            st.subheader(f"Moving Average (50-day) for {ticker.upper()}")
            stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
            st.line_chart(stock_data[['Close', '50_MA']])

        else:
            st.warning("No data found for the given ticker and date range. Please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a valid stock ticker to get started.")
