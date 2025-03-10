import os
import pandas as pd
from dotenv import load_dotenv

"""
Fetch news data from ALPACA endpoint 
"""

# try to import credentials from keys.py; otherwise, load from .env.
try:
    from keys import API_KEY, SECRET_KEY, URL # type: ignore
except ImportError:
    load_dotenv()
    API_KEY = os.getenv("APCA-API-KEY-ID")
    SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
    # a default URL is provided if no URL in env file
    URL = os.getenv("URL", "https://data.alpaca.markets/v1beta1/news")

from client import Client

# initialize the client using the credentials
client = Client(API_KEY, SECRET_KEY, URL)
rest_client = client.api

# generate date strings "06" to "31" for January 2025.
dates = [f"{day:02d}" for day in range(6, 32)]
TIMEFRAME = "1D"

def fetch_news(portfolio):
    """
    Fetches news for each symbol across the specified dates.
    Returns a list of news lists.
    """
    #Loop through symbols in portfolio and fetch news using the rest_client for each day in the dates array, append these to an array
    news_agg = []
    for symbol in portfolio:
        for day in dates:
            news = rest_client.get_news(
                symbol,
                start=f'2025-01-{day}T00:00:00Z',
                end=f'2025-01-{day}T23:59:59Z',
                limit=50
            )
            news_agg.append(news)
    return news_agg


def fetch_prices(portfolio):
    """
    Fetches price bar data for each symbol in the portfolio across the specified dates.
    Returns a list of price bars lists.
    """

    #Loop through symbols in portfolio and fetch prices using the rest_client for each day in the dates array, append these to an array
    prices_agg = []
    for symbol in portfolio:
        for day in dates:
            bars = rest_client.get_bars(
                symbol,
                TIMEFRAME,
                start=f'2025-01-{day}T00:00:00Z',
                end=f'2025-01-{day}T23:59:59Z'
            )
            prices_agg.append(bars)
    return prices_agg


def main():
    SYMBOLS = ['NVDA']
    # --- fetch news data and append to array---
    news_agg = fetch_news(SYMBOLS)
    news_data = []
    for news_list in news_agg:
        for news in news_list:
            news_data.append({
                "date": news.created_at,
                "headline": news.headline,
                "summary": news.summary
            })

    df_news = pd.DataFrame(news_data)
    file_path = os.path.join("data", "news_data.csv")
    df_news.to_csv(file_path, index=False)
    print("Created news_data.csv with", len(df_news), "records.")

    # --- fetch prices data and append to array---
    prices_agg = fetch_prices(SYMBOLS)
    prices_data = []
    for bars in prices_agg:
        for bar in bars:
            prices_data.append({
                "date": bar.t,
                "price": bar.o,
            })

    df_prices = pd.DataFrame(prices_data)
    df_prices['date'] = df_prices['date'].astype(str)
    #Slice date to only include day, month, year
    df_prices['date'] = df_prices['date'].str[:10]

    file_path = os.path.join("data", "prices_data.csv")
    df_prices.to_csv(file_path, index=False)
    print("Created prices_data.csv with", len(df_news), "records.")


if __name__ == "__main__":
    main()
