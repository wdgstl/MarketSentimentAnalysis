import openai
from keys import OPENAI_KEY
import pandas as pd
import ast
import os

client = openai.OpenAI(api_key=OPENAI_KEY)

def format_docs(docs, dates):
    formatted_docs = "\n\n".join([f"{date} Article {i+1}:\n{doc}" for i, (date, doc) in enumerate(zip(dates, docs))])
    return formatted_docs

def get_sentiment_score(docs, dates):
    formatted_docs = format_docs(docs, dates)
    prompt = f"""
    Analyze the following list of articles regarding NVIDIA stock and assign a sentiment score from 0 to 1 that represents their average score.
    - 0 means extremely negative (bearish).
    - 0.5 means neutral.
    - 1 means extremely positive (bullish).
    - You **can and should use any decimal value** between 0 and 1 (e.g., 0.12, 0.73, 0.91), not just fixed increments like 0.25 or 0.5.

    "{formatted_docs}"

    Provide only the sentiment score as a floating point number.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    score = float(response.choices[0].message.content.strip())
    return score

def read_data(path): # returns list of list of docs 
    df = pd.read_csv(path)
    df["text"] = df["text"].apply(ast.literal_eval)  
    return df["text"], df["date"]

def main():
    scores = {}
    docs, dates = read_data(os.path.join("data", "news_data_processed.csv"))
    for articles, date in zip(docs, dates):
        sentiment_score = get_sentiment_score(articles, date)
        print(f"Sentiment Score: {sentiment_score}, {date}")
        scores[date] = sentiment_score
        df = pd.DataFrame(list(scores.items()), columns=['date', 'Sentiment Score'])

    df.to_csv(os.path.join("data", "sentiment_scores.csv"), index=False)

if __name__ == "__main__":
    main()

