from pkg_resources import resource_string

from jinja2 import Template

from visa_application.constants import (
    COVER_TEMPLATE_NAME,
    INSTRUCTION_TEMPLATE_NAME,
)


def _get_template(template_name):
    return Template(
        resource_string(
            'visa_application.templates',
            template_name,
        ).decode()
    )


def get_cover_template():
    return _get_template(COVER_TEMPLATE_NAME)


def get_instruction_template():
    return _get_template(INSTRUCTION_TEMPLATE_NAME)
