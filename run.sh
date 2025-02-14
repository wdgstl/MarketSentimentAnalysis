#!/bin/bash

VENV_DIR="venv"

#If already venv, skip 
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

#activate venv
source $VENV_DIR/bin/activate

#install packages
echo "Installing required Python packages..."
pip3 install -r requirements.txt

#only scrape if the raw data does not already exist
if [ ! -f "data/prices_data.csv" ] || [ ! -f "data/news_data.csv" ]; then
    echo "Scraping Market Data Using Alpaca API"
    python3 scripts/get_news.py
else
    echo "Market data already exists. Skipping scraping."
fi

#following commands run .py files in order to form pipeline
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
