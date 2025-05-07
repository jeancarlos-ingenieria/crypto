import click
from api import get_top_coins
from rich.console import Console
from rich.table import Table

@click.command()
@click.option("--limit", default=10, help="Cantidad de criptomonedas a mostrar")
@click.option("--currency", default="usd", help="Moneda fiat (usd, eur, ars, etc.)")
def top(limit, currency):
    """Muestra el top N de criptomonedas por capitalización de mercado"""
    data = get_top_coins(limit, currency)
    table = Table(title=f"Top {limit} Criptomonedas", show_lines=True)
    table.add_column("Ranking", justify="right")
    table.add_column("Nombre")
    table.add_column("Precio")
    table.add_column("Cambio 24h")

    for coin in data:
        table.add_row(
            str(coin["market_cap_rank"]),
            f"{coin['name']} ({coin['symbol'].upper()})",
            f"{currency.upper()} {coin['current_price']:,.2f}",
            f"{coin['price_change_percentage_24h']:.2f} %"
        )

    Console().print(table)
