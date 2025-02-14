# MarketSentimentAnalysis
## Repository Contents
The contents of this repository are: 
- Data utilized
- Scripts utilized
- Dockerfile
- MIT License
- Readme
- Docker composition
- Required packages
### Software and Platform Section
- Python in Visual Studio Code was used for this project.
- Add-on packages that need to be installed are:
  - alpaca==1.0.0
  - alpaca-py==0.38.0
  - alpaca-trade-api==3.2.0
  - matplotlib==3.10.0
  - numpy==2.2.2
  - openai==1.61.1
  - pandas==2.2.3
  - pillow==11.1.0
  - pydantic==2.10.6
  - pydantic_core==2.27.2
  - python-dotenv==1.0.1
  - scikit-learn==1.6.1
  - scipy==1.15.1
  - tokenizers==0.21.0
  - torch==2.6.0
  - tqdm==4.67.1
- The platform used was Mac.
### A Map of our Documentation
- The Project Folder is structured:
```
MarketSentimentAnalysis/ │-- data/ │ │-- january_news.json │ │-- new_data_processed.csv │ │-- news_data.csv │ │-- price_data_processed.csv │ │-- prices_data.csv │ │-- scripts/ │ │-- pycache/ │ │ │-- client.cpython-311.pyc │ │ │-- client.cpython-313.pyc │ │ │-- keys.cpython-311.pyc │ │ │-- keys.cpython-313.pyc │ │ │-- pushover.cpython-311.pyc │ │ │-- pushover.cpython-313.pyc │ │-- EDA.ipynb │ │-- client.py │ │-- data_preprocessing.py │ │-- get_news.py │ │-- main.py │ │-- models.py │ │-- pushover.py │ │-- .gitignore │-- Dockerfile │-- LICENSE │-- README.md │-- docker-compose.yaml │-- requirements.txt
```
### Instructions for reproducing our results
