import wikipedia # to get info from wikipedia
from rich.console import Console # for colored text
import click # for CLI(Command-line interface)

console = Console()

@click.group()
def main():
    """A basic wikipedia scraper which grabs information from wikipedia.org based on user input."""
    pass

@main.command()
@click.option(
    '--query', '-q',
    prompt="Enter the query for your wikipedia search",
    help="Query for wikipedia search!"
)
@click.option(
    '--sentences', '-s',
    default=2,
    help="Number of sentences to be displayed."
)
@click.option(
    '--lang', '-l',
    default='en',
    help="Language in which the information will be displayed."
)
def fetch(query, sentences, lang):
    """fetches and displays information based on the query passed in."""
    wikipedia.set_lang(lang)

    try:
        console.print(wikipedia.summary(query, sentences=sentences, auto_suggest=False, redirect=True), justify = 'center')
    except wikipedia.PageError:
        console.print(f"[ERROR] Requested [bold]query({query})[/] not found. Please enter a valid [bold]query![/]")
        console.print(
            f"Else try searching for suggested query!-> [green]{wikipedia.suggest(query)}[/]"
        )

if __name__ == "__main__":
    main()