from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

class AlpacaBroker:
    def __init__(self, api_key, secret_key):
        self.client = TradingClient(
            api_key,
            secret_key,
            paper=True   # IMPORTANT
        )

    def buy_market(self, symbol: str, qty: float):
        order = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        return self.client.submit_order(order)