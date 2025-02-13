import pandas as pd
import ast 

def aggregate_articles(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df['date'] = df['date'].str[:10]
    df["text"] = df["headline"].str.cat(df["summary"], sep=": ",  na_rep="")  
    df.drop("headline", axis=1, inplace=True)
    df.drop("summary", axis=1, inplace=True)
    df_aggregated = df.groupby("date", as_index=False).agg({"text": list})
    df_aggregated.to_csv("new_data_processed.csv", index=False)  
    

def fix_prices_dates(path_to_csv):
    df = pd.read_csv(path_to_csv)
    df['date'] = df['date'].str[:10]
    df.to_csv("price_data_processed.csv", index=False)  


if __name__ == "__main__":
    aggregate_articles('/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/news_data.csv')
    fix_prices_dates('/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/prices_data.csv')