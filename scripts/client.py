from alpaca_trade_api.rest import REST
from alpaca.trading.client import TradingClient

"""
Define a client class to allow API requests to ALPACA endpoints
"""

class Client:
    def __init__(self, api_key, secret_key, url):
        #Set up clients to connect to endpoint using keys
        self.trading_client = TradingClient(api_key, secret_key, url_override= url)
        self.api = REST(api_key, secret_key, url, api_version='v2')
        