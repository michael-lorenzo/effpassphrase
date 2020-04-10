import pathlib
import secrets

import click

with open(pathlib.Path(__file__).parent / "eff_large_wordlist.txt") as f:
    words = [word.split()[1] for word in f]


@click.command()
@click.option("-c", "--count", default=6, help="Number of words in the passphrase.")
@click.option(
    "-s",
    "--separator",
    default=" ",
    help="Separator used between words in the passphrase.",
)
def create_passphrase(count, separator):
    click.echo(separator.join(secrets.choice(words) for _ in range(count)))
