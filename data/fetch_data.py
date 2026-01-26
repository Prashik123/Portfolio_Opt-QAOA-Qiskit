import yfinance as yf
import numpy as np

def fetch_returns(tickers, period="2y"):
    prices = yf.download(
        tickers,
        period=period,
        progress=False
    )["Adj Close"]

    returns = prices.pct_change().dropna()
    return returns.values
