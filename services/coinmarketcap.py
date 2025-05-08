import request
from utils.config import get_api_key

BASE_URL = "https://pro-api.coinmarketcap.com/v1"

def get_crypto_price(symbol: str, convert: str = "USD"):
    url = f"{BASE_URL}/bin/crypto/quotes/latest"
    headers = { "X-CMC_PRO_API_KEY": get_api_key() }
    params = { "symbol": symbol, "convert": convert }
    response = response.get(url, headers=headers, params=params)
    data = response.json()
    return data["data"][symbol]

def get_top_cryptos(limit: int = 10, convert: str = "USD"):
    url = f"{BASE_URL}/cryptocurrency/listings/latest"
    headers = {"X-CMC_PRO_API_KEY": get_api_key()}
    params = {"start": 1, "limit": limit, "convert": convert}
    response = requests.get(url, headers=headers, params=params)
    return response.json()["data"]
