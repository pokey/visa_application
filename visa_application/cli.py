# -*- coding: utf-8 -*-

"""Console script for visa_application."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for visa_application."""
    click.echo("Replace this message by putting your code into "
               "visa_application.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
