# MarketSentimentAnalysis
## Repository Contents
The contents of this repository are: 
- Data utilized
- Output files
- Scripts utilized
- .gitgnore file
- Dockerfile
- MIT License
- Readme
- Docker composition
- Required packages
- Bash script to run pipeline
  
### Software and Platform Section
- Langauges: Python, Bash Scripting
- Software: VSCode, Jupyter Notebooks
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
  
MarketSentimentAnalysis/
├── data/
├── output/
├── scripts/
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── run.sh


### Instructions for reproducing our results - Note YOU MUST HAVE AN OPENAI API KEY TO REPRODUCE ANY ANALYSIS
1) Option 1 - Use run.sh bash script
   - Clone github repository
   - Create keys.py in scripts directory with OPENAI_KEY='YOUROPENAIKEY'
   - If you have ALPACA API Keys and want to scrape the data yourself, delete all data in the data directory and add the following to keys.py: SECRET_KEY='ALPACA SECRET KEY', API_KEY='ALPACA API KEY', URL='https://api.alpaca.markets'
   - Change permissions of run.sh in terminal: chmod 700 run.sh
   - Run run.sh in terminal: ./run.sh
   - View time series graph and correlation inside the output directory
   
2) Option 2 - Run python files manually starting with raw data (prices and news csvs)
   - Clone github repository
   - Create a virtual environment: python3 -m venv myvenv
   - Activate venv: source myvenv/bin/activate
   - Install requirements: pip3 install -r requirements.txt
   - Create keys.py in scripts directory with OPENAI_KEY='YOUROPENAIKEY'
   - Starting with two csvs in the data directory: prices_data.csv and news_data.csv, run python3 data_preprocessing.py from inside the scripts directory
   - Next, run python3 get_sentiments.py from inside the scripts directory
   - Then, run python3 post_processing.py from inside the scripts directory
   - Finally, run python3 run_analytics.py to generate the analysis (time series graph and correlation), view output inside the output directory

3) Option 3 - Run python files manually without raw data (pulling using Alpaca)
   - Clone github repository
   - Create a virtual environment: python3 -m venv myvenv
   - Activate venv: source myvenv/bin/activate
   - Install requirements: pip3 install -r requirements.txt
   - Create Alpaca Secret Key and API Key
   - Create keys.py inside scripts directory, create the following variables: SECRET_KEY='ALPACA SECRET KEY', API_KEY='ALPACA API KEY', URL='https://api.alpaca.markets', OPENAI_KEY='YOUROPENAIKEY'
   - Run python3 get_news.py inside the scripts directory
   - Run python3 data_preprocessing.py from inside the scripts directory
   - Next, run python3 get_sentiments.py from inside the scripts directory
   - Then, run python3 post_processing.py from inside the scripts directory
   - Finally, run python3 run_analytics.py to generate the analysis (time series graph and correlation), view output inside the output directory

### Instructions for Live Analysis
1) Build and run Docker container
   - run in terminal: docker compose up --build
