import yfinance as yf
import datetime as dt
import pandas as pd

# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

reliance = yf.Ticker("stock_symbol")
reliance

# Calculate the start and end dates for the historical data (previous 3 months)
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=90)

# Download the historical data using yfinance API

rel_historical = reliance.history(start_date, end_date, interval="15m")
rel_historical

# Save the data to a CSV file
filename = stock_symbol + '_data.csv'
rel_historical.to_csv(filename)
print('Data saved to', filename)
