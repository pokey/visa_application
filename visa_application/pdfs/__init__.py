from pkg_resources import resource_string

from visa_application.constants import COLOR_ITEM_PDF_NAME


def _get_pdf(pdf_name):
    return resource_string('visa_application.pdfs', pdf_name)


def get_color_item_pdf():
    return _get_pdf(COLOR_ITEM_PDF_NAME)
