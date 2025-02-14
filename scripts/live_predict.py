import time
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta
import ast
from get_sentiments import *
from keys import *

"""
Run live predictions on market data
"""

#try to import keys
try:
    from keys import API_KEY, SECRET_KEY, URL  
except ImportError:
    load_dotenv()
    API_KEY = os.getenv("APCA-API-KEY-ID")
    SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")
    URL = os.getenv("URL", "https://data.alpaca.markets/v1beta1/news")

from client import Client

client = Client(API_KEY, SECRET_KEY, URL)
rest_client = client.api


STREAM_URL = 'wss://stream.data.alpaca.markets/v1beta1/news'
SYMBOLS = ['NVDA'] 
FETCH_INTERVAL = 3 * 60 * 60 

#fetch news from the beginning of yesterday to the current time 
def fetch_news():
    yesterday_start = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ')
    today = datetime.now().strftime('%Y-%m-%d')
    #Make one news API call for each symbol in SYMBOLS
    for symbol in SYMBOLS:
        news = rest_client.get_news(symbol, start=yesterday_start, end=today, limit=50)
    news_data = [] 
    #Parse the news data and add to news_data array
    for article in news:
        news_data.append({
            "date": article.created_at,
            "headline": article.headline,
            "summary": article.summary
           })
 
    df_news = pd.DataFrame(news_data)
    #Combine the headline and summary
    df_news["text"] = df_news["headline"].str.cat(df_news["summary"], sep=": ", na_rep="")
    df_news = df_news.drop(columns=["headline", "summary"])
    df_news["date"] = 1
    #Group by the date (which is 1), creating one massive list to run a sentiment model on to get one score 
    df_aggregated = df_news.groupby("date", as_index=False).agg({"text": lambda x: list(x)})
    df_aggregated["text"] = df_aggregated["text"].apply(lambda x: str(x))  
    df_aggregated["text"] = df_aggregated["text"].apply(ast.literal_eval)  
    return df_aggregated

#run the sentiment model
def analyze_sentiment(df):
    score = get_sentiment_score(df["text"], df["date"])
    return score

#format the message to be output
def format_message(score):
    yesterday_start = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    difference_hours = (datetime.now() - yesterday_start).total_seconds() / 3600  # Corrected calculation
    return f"Market news articles about NVIDIA have a sentiment score of {score} (1=bullish, 0=bearish), over the past {difference_hours:.1f} hours."

#loop indefinitely and fetch news and run sentiment every 3 hours 
def predict():
    while True:
        print("Fetching news...")
        df_news = fetch_news()

        if df_news.empty:
            print("No new news found.")
        else:
            print("Analyzing sentiment...")
            score = analyze_sentiment(df_news)
            print(format_message(score))

        print(f"Sleeping for {FETCH_INTERVAL // 3600} hours...")
        #Sleep for FETCH_INTERVAL then fetch again
        time.sleep(FETCH_INTERVAL)

def main():
    predict()

if __name__ == "__main__":
    main()

