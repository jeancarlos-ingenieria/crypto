import click
from commands.price import price

@click.group()
def cli():
    """
    Cryptocurrency CLI tool to get price, top, and other data.
    """
    pass

cli.add_command(price)

if __name__ == '__main__':
    cli()
