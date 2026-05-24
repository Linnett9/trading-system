from abc import ABC, abstractmethod


class IStrategy(ABC):
    """
    Abstract base class for all trading strategies.

    A strategy is responsible ONLY for decision-making.
    It must NOT:
    - place trades
    - access broker APIs
    - manage portfolio state

    It takes market data as input and returns a signal.
    """

    @abstractmethod
    def generate_signal(self, market_data):
        """
        Generate a trading signal from market data.

        Args:
            market_data (dict):
                Example:
                {
                    "symbol": "SPY",
                    "price": 510.25
                }

        Returns:
            str: One of
                - "BUY"
                - "SELL"
                - "HOLD"
        """
        pass