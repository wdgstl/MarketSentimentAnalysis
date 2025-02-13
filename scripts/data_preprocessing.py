import pandas as pd
from datetime import timedelta

def aggregate_articles(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df['date'] = df['date'].str[:10]
    df["date"] = pd.to_datetime(df["date"])
    df["text"] = df["headline"].str.cat(df["summary"], sep=": ", na_rep="")
    df = df.drop(columns=["headline", "summary"])
    def adjust_to_friday(date):
        if date.weekday() == 5:  
            return date - timedelta(days=1)
        elif date.weekday() == 6:  
            return date - timedelta(days=2)
        return date  
    df["date"] = df["date"].apply(adjust_to_friday)
    df_aggregated = df.groupby("date", as_index=False).agg({"text": lambda x: list(x)})
    df_aggregated["text"] = df_aggregated["text"].apply(lambda x: str(x))  
    df_aggregated.to_csv("/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/new_data_processed.csv", index=False)
    
def fix_prices_dates(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df['date'] = df['date'].str[:10]
    df.to_csv("/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/price_data_processed.csv", index=False)  


if __name__ == "__main__":
    aggregate_articles('/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/news_data.csv')
    fix_prices_dates('/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/prices_data.csv')