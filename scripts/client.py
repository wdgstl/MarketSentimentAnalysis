from alpaca_trade_api.rest import REST
from alpaca.trading.client import TradingClient

class Client:
    def __init__(self, api_key, secret_key, url):
        self.trading_client = TradingClient(api_key, secret_key, url_override= url)
        self.api = REST(api_key, secret_key, url, api_version='v2')
        