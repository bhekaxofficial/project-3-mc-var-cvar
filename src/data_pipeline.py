#Step by step process

#1: Download daily adjusted close prices (2015-2024)
#2: Save them to data/raw/prices.csv
#3: Compute log returns
#4: Save them to data/processed/returns.csv


import os
import numpy as np
import pandas as pd
import yfinance as yf


TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN",
    "JPM", "JNJ", "XOM", "SPY"
]

START_DATE = "2015-01-01"
END_DATE = "2024-01-01"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "prices.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "returns.csv")


#Utilities

def ensure_directories():
    os.makedirs("data/raw", exist_ok = True)
    os.makedirs("data/processed", exist_ok = True)

#Step 1: Download Prices: Attached below is the raw data
 
def download_price_data():
    print("Downloading price data...")
    data = yf.download(
        TICKERS,
        start = START_DATE,
        end = END_DATE,
        auto_adjust = True,
        progress = False
    )

    prices = data["Close"]
    prices.to_csv(RAW_DATA_PATH)
    print(f"Saved raw prices to {RAW_DATA_PATH}")
    return prices

#Step 2: Compute log. Below we are going to process the raw data.

def compute_log_returns(prices: pd.DataFrame):
    print("Computing log returns...")
    #log return = log(Today Price / Yesterday Price). It is not log((Pt-Pt-1) / Pt-1) Like I first thought. It is log(1 + (Pt-Pt-1) / Pt-1).
    log_returns = np.log(prices / prices.shift(1))
    log_returns = log_returns.dropna()

    log_returns.to_csv(PROCESSED_DATA_PATH)
    print(f"Saved processed returns to {PROCESSED_DATA_PATH}")

    return log_returns

#Main pipeline

def main():
    ensure_directories()
    prices = download_price_data()
    compute_log_returns(prices)
    print("Data pipeline complete.")

if __name__ == "__main__":
    main()
