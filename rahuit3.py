import yfinance as yf
import pandas as pd

# Define your portfolio
portfolio = {
    "AAPL": 10,  # Apple with 10 shares
    "MSFT": 15,  # Microsoft with 15 shares
    "GOOGL": 5   # Alphabet with 5 shares
}

# Fetch data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")['Close'][0]

# Calculate portfolio value
total_value = 0
for ticker, shares in portfolio.items():
    price = get_stock_data(ticker)
    total_value += price * shares
    print(f"{ticker}: {shares} shares @ {price:.2f} each")

print(f"Total portfolio value: {total_value:.2f}")
