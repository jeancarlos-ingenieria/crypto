import requests

BASE_URL = "https://api.coingecko/api/v3"


def get_price(coin_id, vs_currency="usd"):
    url = f"${BASE_URL}/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": vs_currency,
        "include_24hr_change": "true",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_top_coins(limit=10, vs_currency="usd"):
    url = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
