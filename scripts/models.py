import openai
from keys import OPENAI_KEY

client = openai.OpenAI(api_key=OPENAI_KEY)

def get_sentiment_score(message):
    prompt = f"""
    Analyze the following message regarding NVIDIA stock and assign a sentiment score from 0 to 1.
    - 0 means extremely negative (bearish).
    - 0.5 means neutral.
    - 1 means extremely positive (bullish).
    - You **can and should use any decimal value** between 0 and 1 (e.g., 0.12, 0.73, 0.91), not just fixed increments like 0.25 or 0.5.

    Message: "{message}"

    Provide only the sentiment score as a floating point number.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    score = float(response.choices[0].message.content.strip())
    return score

message = "Dow Rises Over 200 Points Ahead Of Inflation, Earnings Data: Greed Index Remains In 'Fear' Zone"
sentiment_score = get_sentiment_score(message)
print(f"Sentiment Score: {sentiment_score}")

