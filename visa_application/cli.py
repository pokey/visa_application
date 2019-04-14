# -*- coding: utf-8 -*-

"""Console script for visa_application."""
import pathlib
import sys
import tempfile

import click
from PyPDF2 import PdfFileMerger, PdfFileReader

from visa_application.click import make_callback
from visa_application.io import read_index
from visa_application.pdfs import get_color_item_pdf
from visa_application.templates import (
    get_cover_template,
    get_instruction_template,
)
from visa_application.templatized_pdf_generator import TemplatizedPdfGenerator


@click.command()
@click.option(
    '--index',
    '-i',
    type=click.File('r'),
    callback=make_callback(read_index),
    required=True,
)
@click.option(
    '--document-dir',
    '-d',
    type=click.Path(
        file_okay=False,
        exists=True,
    ),
    callback=make_callback(pathlib.Path),
    required=True,
)
@click.option(
    '--black-and-white-output',
    '-b',
    type=click.File('wb'),
)
@click.option(
    '--color-output',
    '-c',
    type=click.File('wb'),
)
def main(index, document_dir, black_and_white_output, color_output):
    """
    Collect documents into a PDF

    """

    cover_generator = TemplatizedPdfGenerator(
        template=get_cover_template(),
    )
    instruction_generator = TemplatizedPdfGenerator(
        template=get_instruction_template(),
    )
    color_item_pdf = get_color_item_pdf()

    black_and_white_merger = PdfFileMerger(strict=False)
    color_merger = PdfFileMerger(strict=False)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = pathlib.Path(temp_dir)

        for i, section in enumerate(index):
            index = i+1
            click.echo(f"{index}. {section.title}")

            cover = cover_generator(
                index=index,
                title=section.title,
            )
            black_and_white_merger.append(PdfFileReader(cover))

            for item in section.items:
                black_and_white_pdf, color_pdf = None, None

                if item.text:
                    click.echo(f"   Text '{item.text}'")
                    black_and_white_pdf = instruction_generator(text=item.text)
                elif item.is_color:
                    click.echo(f"   Reading from '{item.path}' (color)")
                    black_and_white_pdf = color_item_pdf
                    color_pdf = open(document_dir / item.path, 'rb')
                else:
                    click.echo(f"   Reading from '{item.path}' (B&W)")
                    black_and_white_pdf = open(document_dir / item.path, 'rb')

                if black_and_white_pdf:
                    black_and_white_merger.append(
                        PdfFileReader(black_and_white_pdf)
                    )
                if color_pdf:
                    color_merger.append(PdfFileReader(color_pdf))

            click.echo()

        black_and_white_merger.write(black_and_white_output)
        color_merger.write(color_output)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
