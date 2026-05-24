from core.strategy.strategy import IStrategy


class SimpleStrategy(IStrategy):
    """
    A minimal rule-based trading strategy.

    This is NOT meant to be profitable.
    It exists to validate the system architecture.

    Logic:
    - If price < threshold → BUY
    - If price > threshold → SELL
    - Otherwise → HOLD
    """

    def __init__(self, threshold=500):
        """
        Args:
            threshold (float):
                A reference price used for decision making.
                In real systems this would be replaced by:
                - indicators (RSI, MA, etc.)
                - or ML model outputs
        """
        self.threshold = threshold

    def generate_signal(self, market_data):
        """
        Convert market data into a trading signal.

        Args:
            market_data (dict):
                Must contain:
                - "price" (float)

        Returns:
            str: BUY / SELL / HOLD
        """

        price = market_data["price"]

        # Basic decision rules
        if price > self.threshold:
            return "SELL"

        elif price < self.threshold:
            return "BUY"

        else:
            return "HOLD"