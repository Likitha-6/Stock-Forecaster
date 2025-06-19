import yfinance as yf
import pandas as pd

def load_stock_data(ticker, start="2020-01-01"):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start)
    df = df[["Close"]]
    df.reset_index(inplace=True)
    return df
