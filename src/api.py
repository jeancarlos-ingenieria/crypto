import requests
from dotenv import load_dotenv
import os

# Cargar la API Key desde el archivo .env
load_dotenv()
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

BASE_URL = "https://pro-api.coinmarketcap.com/v1"

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY,
}


# Función para obtener el precio de la criptomoneda
def get_crypto_price(crypto, vs_currency="usd"):
    """
    Get the current price of a cryptocurrency in the given currency.
    """
    # Validar moneda de comparación
    valid_currencies = ["usd", "eur", "gbp", "ars", "btc", "eth", "jpy", "cny"]
    if vs_currency.lower() not in valid_currencies:
        raise ValueError(
            f"Invalid currency: {vs_currency}. Supported currencies: {', '.join(valid_currencies)}"
        )

    url = f"{BASE_URL}/cryptocurrency/quotes/latest"
    params = {"symbol": crypto.upper(), "convert": vs_currency.upper()}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Esto lanzará un error si la respuesta no es 200 OK
    return response.json()
