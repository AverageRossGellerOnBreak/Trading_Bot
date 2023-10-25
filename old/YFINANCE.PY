import yfinance as yf
import pandas as pd
from datetime import datetime


# CREATE TICKER INSTANCE FOR A STOCK
stock_symbol = input("Enter the stock symbol: ")
stock_ticker = yf.Ticker(stock_symbol)

# GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
end_date = datetime.now().strftime('%Y-%m-%d')
stock_symbol_hist = stock_ticker.history(start='2023-05-01',end=end_date,interval='15m')



# Save the data to a CSV file
filename = stock_symbol + '_data.csv'
stock_symbol_hist.to_csv(filename)
print('Data saved to', filename)


