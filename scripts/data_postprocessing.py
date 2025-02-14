import pandas as pd
import os

def merge_dfs(path1, path2):
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    df1['date'] = pd.to_datetime(df1['date'])
    df2['date'] = pd.to_datetime(df2['date'])
    merged_df = pd.merge(df1, df2, on="date", how="inner")
    return merged_df

def shift_prices_down(df):
    df = df.copy()  
    df['Next Day Price'] = df['price'].shift(-1)
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
