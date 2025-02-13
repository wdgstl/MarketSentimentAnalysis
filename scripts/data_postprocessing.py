import pandas as pd

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
    df.to_csv("/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/scores_with_prices.csv", index=False)
    return df

if __name__ == "__main__":
    p1 = '/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/sentiment_scores.csv'
    p2 = '/Users/wdgstl/UVA/DS/MarketSentimentAnalysis/data/price_data_processed.csv'

    merged_df = merge_dfs(p1, p2)

    adjusted_df = shift_prices_down(merged_df)
