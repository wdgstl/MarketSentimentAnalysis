import pandas as pd
import os

"""
Post process data for analysis
"""

#merge the prices dataset with the scores dataset
def merge_dfs(path1, path2):
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    df1['date'] = pd.to_datetime(df1['date'])
    df2['date'] = pd.to_datetime(df2['date'])
    #Inner merge the datasets such that only matching elements remiain 
    merged_df = pd.merge(df1, df2, on="date", how="inner")
    return merged_df

#adjust the dataset such that a row contains the current day score, along with the next day opening price
def shift_prices_down(df):
    df = df.copy()  
    #Shift the prices so that the next day price is in the row of the current day
    df['Next Day Price'] = df['price'].shift(-1)
    #Calculate price delta as next day price - current day 
    df['Price Delta'] = df['Next Day Price'] - df['price']
    df = df.dropna().reset_index(drop=True)
    df.to_csv(os.path.join("data", "scores_with_prices.csv"), index=False)
    print("Created scores_with_prices.csv with", len(df), "records.")
    return df

def main():
    merged_df = merge_dfs(os.path.join("data", "sentiment_scores.csv"), os.path.join("data", "prices_data.csv"))
    adjusted_df = shift_prices_down(merged_df)

if __name__ == "__main__":
   main()
