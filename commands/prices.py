import click
from services.coinmarketcap import get_crypto_price
from utils.display import print_price_info

@click.command()
@click.argument("symbol")
@click.option("--currency", "-c", default="USD")

