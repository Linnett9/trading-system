from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


class AlpacaBroker:
    """
    Thin wrapper around Alpaca TradingClient.

    Responsibility:
    - Translate internal trading engine requests
      into Alpaca order requests

    Does NOT:
    - contain strategy logic
    - manage portfolio state
    """

    def __init__(self, api_key: str, secret_key: str):
        self.client = TradingClient(
            api_key,
            secret_key,
            paper=True  # paper trading mode
        )

    def buy_market(self, symbol: str, qty: float):
        """
        Submit a market BUY order
        """
        order = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        return self.client.submit_order(order)

    def sell_market(self, symbol: str, qty: float):
        """
        Submit a market SELL order
        """
        order = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        return self.client.submit_order(order)