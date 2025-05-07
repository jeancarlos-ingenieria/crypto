import click
from api import get_price
from rich import print


@click.command()
@click.argument("coin_id")
@click.option("--currency", default="usd", help="Moneda fiat")
def price(coin_id, currency):
    """Muestra el precio actual de una cripto"""
    data = get_price(coin_id, currency)
    if coin_id in data:
        price = data[coin_id][currency]
        change = data[coin_id].get(f"{currency}_24h_change", 0)
        print(
            f"[bold cyan]{coin_id.upper()}[/bold cyan]: {currency.upper()} {price:,.2f} | 24h cambio: {change:.2f}%"
        )
    else:
        print(f"[red]Criptomoneda '{coin_id}' no encontrada[/red]")

