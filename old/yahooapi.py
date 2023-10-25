import yfinance as yf
import datetime as dt
import pandas as pd

# Input the stock symbol
stock_symbol = input("Enter the stock symbol: ")

# Calculate the start and end dates for the historical data (previous 3 months)
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=90)

# Download the historical data using yfinance API
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save the data to a CSV file
filename = stock_symbol + '_data.csv'
stock_data.to_csv(filename)
print('Data saved to', filename)
