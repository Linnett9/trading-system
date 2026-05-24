import os
from dotenv import load_dotenv
from infrastructure.brokers.alpaca_broker import AlpacaBroker

# Load environment variables from .env file (recommended)
load_dotenv()

print("=== STARTING FIRST TRADE ===")

# 1. Load config (API keys from environment)
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")

print("Keys loaded:", API_KEY is not None, SECRET_KEY is not None)

# Safety check (fail fast instead of silent None errors)
if not API_KEY or not SECRET_KEY:
    raise ValueError("Missing API keys. Check your .env or environment variables.")

# 2. Connect to broker (paper trading)
broker = AlpacaBroker(API_KEY, SECRET_KEY)
print("Broker connected")

# 3. Submit order
symbol = "SPY"
qty = 1

print(f"Submitting order: BUY {qty} {symbol}")

response = broker.buy_market(symbol, qty)

# 4. Output result
print("ORDER RESPONSE:")
print(response)

print("=== DONE ===")