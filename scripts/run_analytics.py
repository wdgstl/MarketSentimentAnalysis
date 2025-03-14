from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np 

"""
Run and plot analytics on final dataset
"""

#generate a time series model: Sentiment Scores and Opening Day Prices
def plot_time_series(path):
    df = pd.read_csv(path)
    #Use the scaler to scale the price and score so they fit together in the time series 
    scaler = MinMaxScaler()
    df[["score_norm", "price_norm"]] = scaler.fit_transform(df[["Sentiment Score", "price"]])
    #Plot the score and prices together
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["score_norm"], marker='o', linestyle='-', label="Sentiment Score", color='blue')
    plt.plot(df["date"], df["price_norm"], marker='s', linestyle='-', label="Stock Price", color='red')
    #Set Labels
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Sentiment Score vs. Opening Price (Time Series)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()

    plt.savefig(os.path.join("output", "time_series_plot.png"), bbox_inches="tight")
    plt.close()  
    print(f"Time series plot saved as {os.path.join("output", "time_series_plot.png")}")


#generate Pearson correlation coefficient and scatterplot 
def plot_correlation(path):
    df = pd.read_csv(path)
    #Use the scaler to scale the price and score so they fit together in scatter
    scaler = MinMaxScaler()
    df[["score_norm", "price_norm"]] = scaler.fit_transform(df[["Sentiment Score", "Next Day Price"]])
    #Calculate Pearson Correlation Coefficient and Line of Best Fit
    correlation = np.corrcoef(df["score_norm"], df["price_norm"])[0, 1]
    m, b = np.polyfit(df["score_norm"], df["price_norm"], 1)
    #Plot the scores and prices in a scatterplot 
    plt.figure(figsize=(8, 6))
    plt.scatter(df["score_norm"], df["price_norm"], alpha=0.7, color='blue', label="Data points")
    plt.plot(df["score_norm"], m * df["score_norm"] + b, color='red', label="Best-fit line")  # Regression line
    #Add Labels 
    plt.xlabel("Sentiment Score (Normalized)")
    plt.ylabel("Next Day Opening Price (Normalized)")
    plt.title(f"Scatter Plot of Sentiment Score vs. Next Day Opening Price\nCorrelation: {correlation:.2f}")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join("output", "correlation_plot.png"), bbox_inches="tight")
    plt.close()  
    print(f"Correlation plot saved as {os.path.join("output", "correlation_plot.png")}")


def main():
    plot_time_series(os.path.join("data", "scores_with_prices.csv"))
    plot_correlation(os.path.join("data", "scores_with_prices.csv"))


if __name__ == "__main__":
    main()