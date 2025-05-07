import click
from rich.console import Console
from rich.table import Table
from api import get_crypto_price

console = Console()


@click.command()
@click.argument("crypto")
@click.option(
    "--vs-currency", default="usd", help="Currency to compare against, default is USD."
)
@click.option(
    "--refresh-interval",
    default=0,
    help="Set the interval to refresh data (in seconds).",
)
@click.option(
    "--output-format", default="table", help="Output format: table, json, csv"
)
def price(crypto, vs_currency, refresh_interval, output_format):
    """
    Get the current price of a cryptocurrency.
    """
    try:
        vs_currency = vs_currency.upper()

        # Obtén los datos usando la API
        data = get_crypto_price(crypto, vs_currency)

        if "data" not in data or crypto.upper() not in data["data"]:
            raise Exception(f"Error: Could not find data for {crypto.upper()}")
        # Acceder a los datos de la criptomoneda
        crypto_data = data["data"][crypto.upper()]

        # Mostrar resultados según el formato solicitado
        if output_format == "table":
            table = Table(title=f"{crypto.upper()} Price")
            table.add_column("Attribute", justify="right", style="cyan")
            table.add_column("Value", justify="left", style="magenta")

            table.add_row("Price", f"${crypto_data['quote'][vs_currency]['price']:.2f}")
            table.add_row(
                "Market Cap", f"${crypto_data['quote'][vs_currency]['market_cap']:.2f}"
            )
            table.add_row(
                "24h Change",
                f"{crypto_data['quote'][vs_currency]['percent_change_24h']:.2f}%",
            )

            console.print(table)

        elif output_format == "json":
            import json

            console.print(json.dumps(data, indent=4))

        elif output_format == "csv":
            import csv

            writer = csv.DictWriter(console.file, fieldnames=["Attribute", "Value"])
            writer.writeheader()
            writer.writerows(
                [
                    {
                        "Attribute": "Price",
                        "Value": f"${crypto_data['quote'][vs_currency]['price']:.2f}",
                    },
                    {
                        "Attribute": "Market Cap",
                        "Value": f"${crypto_data['quote'][vs_currency]['market_cap']:.2f}",
                    },
                    {
                        "Attribute": "24h Change",
                        "Value": f"{crypto_data['quote'][vs_currency]['percent_change_24h']:.2f}%",
                    },
                ]
            )
            console.print("Data exported to CSV.")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")


if __name__ == "__main__":
    price()
