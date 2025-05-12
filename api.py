import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def get_price(crypto: str, coin: str = "usd") -> dict:
