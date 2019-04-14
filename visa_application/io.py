import yaml

from visa_application.models.section import Section


def read_index(index):
    return [
        Section.from_dict(section_dict)
        for section_dict in yaml.load(index)
    ]
