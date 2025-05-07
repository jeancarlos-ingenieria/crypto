import click
from commands.price import price
from commands.top import top

@click.group()
def cli():
    """Herramienta CLI de criptomonedas"""
    pass

cli.add_command(price)
cli.add_command(top)

if __name__ == "__main__":
    cli()
