#!/bin/bash

VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

echo "Installing required Python packages..."
pip3 install -r requirements.txt

if [ ! -f "data/prices_data.csv" ] || [ ! -f "data/news_data.csv" ]; then
    echo "Scraping Market Data Using Alpaca API"
    python3 scripts/get_news.py
else
    echo "Market data already exists. Skipping scraping."
fi

echo "Preprocessing Market Data"
python3 scripts/data_preprocessing.py

echo "Generating Sentiment Scores For Market News Using gpt4-turbo"
python3 scripts/get_sentiments.py

echo "Post Processing Sentiment Data"
python3 scripts/data_postprocessing.py

echo "Running Analytics on Sentiment Data"
python3 scripts/run_analytics.py

# Deactivate virtual environment
deactivate

echo "Script execution complete."
