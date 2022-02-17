import click


@click.command()
@click.option("-a", type=int)
@click.option("-b", type=int)
def add_two(a, b):
    print(a + b)
