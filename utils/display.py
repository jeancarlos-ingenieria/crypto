from rich.console import console
from rich.table import Table

console = Console()

def print_price_info(crypto: str, convet:str ="USD"):
        quote = crypto["quote"][convert]
        table = Table(
            title=f"{crypto['name']} ({crypto['symbol']})", 
                  show_header=True, 
                  header_style="bold magenta"
            )
    table.add_column("Price", justify="right")
    table.add_column("Change 1h", justify="right")
    table.add_column("Change 24h", justify="right")
    table.add_column("Change 7d", justify="right")
    table.add_row(
        f"{quote['price']:.2f}",
        f"{quote['percent_change_1h']:.2f}%",
        f"{quote['percent_change_24h']:.2f}%",
        f"{quote['percent_change_7d']:.2f}%"
    )
    console.print(table)

def print_top_cryptos(data, convert="USD"):
    table = Table(
            title=f"Top {len(data)} Cryptos ({convert})",
                  header_style="bold blue"
            )
    table.add_column("Rank")
    table.add_column("Name")
    table.add_column("Symbol")
    table.add_column("Price", justify="right")
    for item in data:
        quote = item["quote"][convert]
        table.add_row(
            str(item["cmc_rank"]),
            item["name"],
            item["symbol"],
            f"{quote['price']:.2f}"
        )
    console.print(table)
