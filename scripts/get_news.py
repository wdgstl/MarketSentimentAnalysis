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

#Jan 4 to Feb 4 


news_agg = []
def fetch_news(portfolio):
    for src in portfolio:
        for n in range(1, 7):
            news = rest_client.get_news(src, start=f'2025-01-0{n}T00:00:00Z', end=f'2022-01-0{n}T23:59:59Z', limit=50)
            news_agg.append(news)
    return news_agg



if __name__ == "__main__":
    SYMBOL = ['NVDA']
    news =  fetch_news(SYMBOL)
    for n in news_agg:
        print(len(n))
