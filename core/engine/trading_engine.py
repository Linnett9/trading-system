class TradingEngine:
    """
    Orchestrates the entire trading flow.

    This is the "brain" of the system:
    - gets market data
    - asks strategy for decision
    - sends orders via broker
    """

    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run_once(self, market_data):
        """
        Executes one full decision cycle.
        """

        # 1. Get signal from strategy
        signal = self.strategy.generate_signal(market_data)
        print("Strategy signal:", signal)

        symbol = market_data["symbol"]
        qty = 1

        # 2. Route to broker
        if signal == "BUY":
            return self.broker.buy_market(symbol, qty)

        elif signal == "SELL":
            return self.broker.sell_market(symbol, qty)

        else:
            return "NO TRADE"