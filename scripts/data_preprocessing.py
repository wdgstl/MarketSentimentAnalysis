import pandas as pd
from datetime import timedelta
import os

"""
Preprocess the prices and news data 
"""

#Aggregrate the news articles by date - create a list of articles for a given date
def aggregate_articles(path_to_csv):
    df = pd.read_csv(path_to_csv)
    #slice the time to only the day, year, and month
    df['date'] = df['date'].str[:10]
    df["date"] = pd.to_datetime(df["date"])
    #combine headline and summary
    df["text"] = df["headline"].str.cat(df["summary"], sep=": ", na_rep="")
    df = df.drop(columns=["headline", "summary"])
    #function to combine saturday and sunday to friday, since market closed on weekend
    def adjust_to_friday(date):
        if date.weekday() == 5:  
            return date - timedelta(days=1)
        elif date.weekday() == 6:  
            return date - timedelta(days=2)
        return date  
    df["date"] = df["date"].apply(adjust_to_friday)
    df_aggregated = df.groupby("date", as_index=False).agg({"text": lambda x: list(x)})
    df_aggregated["text"] = df_aggregated["text"].apply(lambda x: str(x))  
    file_path = os.path.join("data", "news_data_processed.csv")
    df_aggregated.to_csv(file_path, index=False)
    print("Created new_data_processed.csv with", len(df_aggregated), "records.")

    
def main():
    aggregate_articles(os.path.join("data", "news_data.csv"))

if __name__ == "__main__":
    main()