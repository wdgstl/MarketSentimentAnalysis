import numpy as np
import pandas as pd
from keys import *
from client import *
from pushover import *
from alpaca_trade_api import Stream 

import time
from datetime import datetime, timedelta

#Define Constants 

STREAM_URL = 'wss://stream.data.alpaca.markets/v1beta1/news'
client = client(API_KEY, SECRET_KEY, URL)
rest_client = client.api
# push = pushover(PUSH_API_TOKEN, USER_KEY)

#Function to Fetch News Daily 

#plot opening price 

#Jan 6 to 31 

#FETCH OPENING PRICES

#MODIFY LOOP TO WORK FOR TIMEFRAME

#USE OPENAI GPT

dates = ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
TIMEFRAME = "1D"

news_agg = []
def fetch_news(portfolio):
    for src in portfolio:
        for n in dates:
            news = rest_client.get_news(src, start=f'2025-01-{n}T00:00:00Z', end=f'2025-01-{n}T23:59:59Z', limit=50)
            news_agg.append(news)
    return news_agg

prices_agg = []
def fetch_prices(portfolio):
    for src in portfolio:
        for n in dates:
            prices = rest_client.get_bars(src, TIMEFRAME, start=f'2025-01-{n}T00:00:00Z', end=f'2025-01-{n}T23:59:59Z')
            prices_agg.append(prices)
    return prices_agg




if __name__ == "__main__":
    SYMBOL = ['NVDA']
    #GET NEWS DATA
    news_agg =  fetch_news(SYMBOL)
    news_data = []
    for n in news_agg:
        for news in n:
            news_data.append({
                "date": news.created_at,
                "headline": news.headline,
                "summary": news.summary
            })

    df_news = pd.DataFrame(news_data)

    df_news.to_csv("news_data.csv", index=False)  

    #GET PRICES DATA 
    prices_agg = fetch_prices(SYMBOL)
    prices_data = []
    for p in prices_agg:
        for price in p:
            prices_data.append({
                 "date": price.t,
                 "price": price.o,
             })
    df_prices = pd.DataFrame(prices_data)

    df_prices.to_csv("prices_data.csv", index=False)  

         


    