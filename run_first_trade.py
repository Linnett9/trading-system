import os
from dotenv import load_dotenv

from infrastructure.brokers.alpaca_broker import AlpacaBroker
from core.strategy.simple_strategy import SimpleStrategy
from core.engine.trading_engine import TradingEngine

# Load .env file
load_dotenv()

print("=== STARTING ENGINE TRADE ===")

# 1. Load API keys
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")

print("Keys loaded:", API_KEY is not None, SECRET_KEY is not None)

if not API_KEY or not SECRET_KEY:
    raise ValueError("Missing API keys")

# 2. Create broker (execution layer)
broker = AlpacaBroker(API_KEY, SECRET_KEY)
print("Broker connected")

# 3. Create strategy (decision layer)
strategy = SimpleStrategy(threshold=500)

# 4. Create engine (orchestration layer)
engine = TradingEngine(strategy=strategy, broker=broker)

# 5. Fake market data (for now)
market_data = {
    "symbol": "SPY",
    "price": 510
}

print("Market data:", market_data)

# 6. Run full system
result = engine.run_once(market_data)

# 7. Output result
print("EXECUTION RESULT:")
print(result)

print("=== DONE ===")